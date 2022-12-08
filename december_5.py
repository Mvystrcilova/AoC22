from december_2 import read_file

def get_current_setting(f):
    stacks = {k: [] for k in range(1,10)}
    line_index = 0
    for line in f:
        if line != '\n':
            line = line[:-1]
            crates = [line[j:j+3] for j in range(len(line)) if (j%4 == 0)]
            for i, crate in enumerate(crates):
                if crate != '   ':
                    stacks[i+1].append(crate)
            line_index += 1
        else:
            break
    return line_index, stacks


def do_move(num_of_crates, source, dest, stacks):
    taken_cranes = stacks[source][:num_of_crates]
    stacks[source] = stacks[source][num_of_crates:]
    for crate in taken_cranes[::-1]:
        stacks[dest].insert(0, crate)
    # stacks[dest].append(list(reversed(taken_cranes)))


def read_line(line):
    line_list = line.split(' ')
    num_of_crates = int(line_list[1])
    source = int(line_list[3])
    dest = int(line_list[5])

    return num_of_crates, source, dest


def get_result(file):
    f = read_file(file)
    line_index, stacks = get_current_setting(f)
    for line in f:
        num_of_crates, source, dest = read_line(line[:-1])
        do_move(num_of_crates, source, dest, stacks)
    for k, v in stacks.items():
        print(f'{k}: {v}')

if __name__ == '__main__':
    get_result('./data/input_5.txt')

