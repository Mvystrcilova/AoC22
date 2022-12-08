from december_2 import read_file


def compare_intervals(interval0, interval1):
    if (int(interval0[0]) <= int(interval1[0])) and (int(interval0[1]) >= int(interval1[1])):
        return 1
    elif (int(interval1[0]) <= int(interval0[0])) and (int(interval1[1]) >= int(interval0[1])):
        return 1
    else:
        return 0


def get_no_overlap(interval0, interval1):
    if int(interval0[1]) < int(interval1[0]):
        return 0
    elif int(interval1[1]) < int(interval0[0]):
        return 0
    print(interval0)
    print(interval1)
    print()
    return 1


def get_intervals(line):
    interval0, interval1 = line.split(',')
    interval0 = interval0.split('-')
    interval1 = interval1.split('-')
    return interval0, interval1


def get_result(file):
    f = read_file(file)
    total_sum = 0
    for line in f:
        int0, int1 = get_intervals(line[:-1])
        complete_overlap = get_no_overlap(int0, int1)
        total_sum += complete_overlap

    print(total_sum)


if __name__ == '__main__':
    get_result('./data/input_4_2.txt')