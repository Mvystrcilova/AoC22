from december_2 import read_file


def split(word):
    word_list = list(word)
    length = len(word_list)
    half0 = word_list[:int(length/2)]
    half1 = word_list[int(length/2):]

    return half0, half1


def get_duplicate_char(half0, half1):
    half0 = set(half0)
    half1 = set(half1)
    intersection = half0.intersection(half1)
    return intersection


def get_char_value(character):
    ascii_value = ord(character)
    if ascii_value < 97:
        return ascii_value - 64 + 26
    else:
        return ascii_value - 96


def get_task2_result(file):
    f = read_file(file)
    group = []
    total_sum = 0
    for line in f:
        if len(group) == 2:
            group1, group2 = group
            group3 = set(line[:-1])
            group = []
            shared = group3.intersection(group1).intersection(group2)
            for character in shared:
                ascii_value = get_char_value(character)
                total_sum += ascii_value

        else:
            group.append(set(line[:-1]))
    print(total_sum)

def get_result(file):
    f = read_file(file)
    total_sum = 0
    for line in f:
        half0, half1 = split(line[:-1])
        intersection = get_duplicate_char(half0, half1)
        for character in intersection:
            ascii_value = get_char_value(character)
            total_sum += ascii_value
    print(total_sum)


if __name__ == '__main__':
    get_task2_result('data/input_3.txt')
