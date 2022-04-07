from typing import Iterable


def interleave(*args: Iterable) -> list:
    """
    :param args: Iterables.
    :return: List with zipped values.
    """
    return split_zipped_list(list(zip(*args)))


def split_zipped_list(zipped_list: list[Iterable]) -> list:
    """
    Accept list of Iterables and extract all values to one list.
    :param zipped_list: List of lists.
    :return: One lists from all lists.
    """
    return [item for sub_list in zipped_list for item in sub_list]


if __name__ == '__main__':
    print(interleave('abc', [1, 2, 3], ('!', '@', '#')))
    print(interleave('abc', [1, 2, 3], ('!', '@', '#'), 'yinon'))
