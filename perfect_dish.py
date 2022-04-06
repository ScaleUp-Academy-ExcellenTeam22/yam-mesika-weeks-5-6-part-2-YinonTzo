import math
import itertools
from typing import Any, Generator


def sum_of_factors(num: int) -> int:
    """
    Sum all dividers of num.
    The dividers of some number must be combination of the prime numbers
    that built it.
    for example fi(18) =  18/2 =9,
                          9/3 = 2
    so we got: 18 = (2^1)*(3^2).
    Now, we want to sum all combination from (2^0)*(3^0),(2^0)*(3^1) and so on.
    So, the function does this calculate:
    (1 + p1) * (1 + p2 + p2^2)
    Where p1 = 2 and p2 = 3 and 18 = (2^1)*(3^2).
    For more explanation read this articles:
    https://www2.math.upenn.edu/~deturck/m170/wk3/lecture/sumdiv.html
    https://www.geeksforgeeks.org/sum-factors-number/
    :param num: Number to find his dividers and sum all of them.
    :return: Sum all dividers.
    """
    res = 1
    for i in range(2, int(math.sqrt(num) + 1)):

        curr_sum = 1
        curr_term = 1

        while num % i == 0:
            num = num / i

            curr_term = curr_term * i
            curr_sum += curr_term

        res = res * curr_sum

    if num > 2:
        res = res * (1 + num)

    return res


def perfect_dish(roll_size: int) -> int:
    """
    Takes some division of roll and subtracts the option to divide 1 piece to someone.
    :param roll_size: The size of roll.
    :return: Sum of all dividers without the option to divide 1 piece to someone.
    """
    return sum_of_factors(roll_size) - roll_size


def is_perfect_dish(roll_size: int) -> bool:
    """
    Check if some division is perfect.
    :param roll_size: The Size of roll to divide.
    :return: If This size is perfect.
    """
    return perfect_dish(roll_size) == roll_size


def find_all_perfect_dish() -> Generator[int, Any, None]:
    """
    Pipeline of all possible sizes to perfect dish.
    When it finds some perfect size it generates the size.
    :return: Perfect sizes.
    """
    return (size for size in generate_all_numbers_from_one() if is_perfect_dish(size))


def generate_all_numbers_from_one() -> Generator:
    """
    https://note.nkmk.me/en/python-itertools-count-cycle-repeat/
    :return: all Numbers from 1
    """
    return (i for i in itertools.count(1))


def perfect_dish_to_division() -> None:
    """
     Does the main task.
     https://github.com/PythonFreeCourse/Notebooks/blob/master/week05/3_Generators.ipynb
     Prints infinitive numbers where every number equals to his dividers-number.
     For example - 28 = 1 + 2 + 4 + 7 + 14.
    """
    for perfect_size in find_all_perfect_dish():
        print(perfect_size)


if __name__ == '__main__':
    perfect_dish_to_division()

