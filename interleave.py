def interleave(*args):
    return split_zipped_list(list(zip(*args)))


def split_zipped_list(zipped_list):
    return [item for sub_list in zipped_list for item in sub_list]


if __name__ == '__main__':
    print(list(interleave('abc', [1, 2, 3], ('!', '@', '#'))))
    print(list(interleave('abc', [1, 2, 3], ('!', '@', '#'), 'yinon')))
