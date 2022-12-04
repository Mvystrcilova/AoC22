

def read_file(file):
    f = open(file)
    return f

# X for Rock, Y for Paper, and Z for Scissors
# A for Rock, B for Paper, and C for Scissors
# X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win


def get_score_for_pair(pair):
    if pair[-2] == 'X':
        if pair[0] == 'A':
            score = 0 + 3
        elif pair[0] == 'B':
            score = 0 + 1
        elif pair[0] == 'C':
            score = 0 + 2
        return score

    elif pair[-2] == 'Y':
        if pair[0] == 'A':
            score = 3 + 1
        elif pair[0] == 'B':
            score = 3 + 2
        elif pair[0] == 'C':
            score =  3 + 3
        return score
    elif pair[-2] == 'Z':
        if pair[0] == 'A':
            score = 6 + 2
        elif pair[0] == 'B':
            score = 6 + 3
        elif pair[0] == 'C':
            score = 6 + 1
        return score

def get_result(f):
    total_score = 0
    for line in f:
        total_score += get_score_for_pair(line)
    print(total_score)


if __name__ == '__main__':
    f = read_file('data/input_2.txt')
    get_result(f)