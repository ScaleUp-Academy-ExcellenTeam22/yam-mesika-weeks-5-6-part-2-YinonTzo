from typing import Iterable, Any, Generator


def interleave(*args: Iterable) -> Generator[Any, Any, None]:
    """
    :param args: Iterables.
    :return:Generator of List with zipped values.
    """
    return split_zipped_list(list(zip(*args)))


def split_zipped_list(zipped_list: list[Iterable]) -> Generator[Any, Any, None]:
    """
    Accept list of Iterables and extract all values to one list.
    :param zipped_list: List of lists.
    :return:Generator of One lists from all lists.
    """
    return (item for sub_list in zipped_list for item in sub_list)


if __name__ == '__main__':
    interleave1 = interleave('abc', [1, 2, 3], ('!', '@', '#'))

    for item in interleave1:
        print(item)
