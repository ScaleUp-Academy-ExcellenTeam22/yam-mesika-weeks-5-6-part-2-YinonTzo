import time
from typing import Iterable


def build_words_list(file_name: str) -> list:
    """
    Open the file and return all words as a list.
    :param file_name: File_text to read words.
    :return: List with all words as values.
    """
    with open(file_name, 'r') as file_descriptor:
        return file_descriptor.read().split()


def build_words_set(file_name: str) -> set:
    """
    Open the file and return all words as a set.
    :param file_name: File_text to read words.
    :return: Set with all words as values.
    """
    with open(file_name, 'r') as file_descriptor:
        return set(file_descriptor.read().split())


def find_word(iterable: Iterable, word: str) -> bool:
    """
    :param iterable: Data structure to make search.
    :param word: A word to find.
    :return: True if the word exist else False.
    """
    return word in iterable


def sum_how_long_to_search(iterable: Iterable) -> float:
    """
    :param iterable: Data structure to make search.
    :return: How much time it took to make one search.
    """
    start_time = time.time()
    find_word(iterable, "zwitterion")
    end_time = time.time()
    return end_time - start_time


def average_runtime(iterable: Iterable) -> float:
    """
    :param iterable: Data structure to make search.
    :return: The average of the amounts of time it took to make 1000 searches.
    """
    count = 0
    for _ in range(1000):
        count += sum_how_long_to_search(iterable)
    return count / 1000


if __name__ == '__main__':
    words_list = build_words_list("words.txt")
    words_set = build_words_set("words.txt")

    amount_of_list_time = average_runtime(words_list)
    amount_of_set_time = average_runtime(words_set)

    print(amount_of_list_time)
    print(amount_of_set_time)
