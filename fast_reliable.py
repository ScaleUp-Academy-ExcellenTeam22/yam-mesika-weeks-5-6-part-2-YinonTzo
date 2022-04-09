def build_words_list_from_file_words(file_name: str) -> list:
    """
    :param file_name: File_text to read words.
    :return: List with all words as values.
    """
    with open(file_name, 'r') as fdr:
        return fdr.read().split()


def build_words_set_from_file_words(file_name: str) -> set:
    """
    :param file_name: File_text to read words.
    :return: Set with all words as values.
    """
    with open(file_name, 'r') as fdr:
        return set(fdr.read().split())


if __name__ == '__main__':
    li = build_words_list_from_file_words("stam.txt")
    se = build_words_set_from_file_words("stam.txt")
    print(li)
    print(se)
