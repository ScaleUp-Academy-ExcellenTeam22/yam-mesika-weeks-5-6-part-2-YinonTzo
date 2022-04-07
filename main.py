import interleave

if __name__ == '__main__':
    interleave1 = interleave.interleave('abc', [1, 2, 3], ('!', '@', '#'))

    for item in interleave1:
        print(item)


