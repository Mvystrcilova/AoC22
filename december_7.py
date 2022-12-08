from december_2 import read_file
def read_command(command, current_dirs, closed_dirs):
    if command.startswith('$ cd') and '..' not in command:
        directory = command.split(' ')[2]
        current_dirs[directory] = 0
        print(f'{command} added new dir: {directory}', len(current_dirs))
    elif command.startswith('$ cd ..'):
        finished_dir = current_dirs.popitem()
        print(f'{command} popping last dir: {finished_dir[0]}', len(current_dirs))
        closed_dirs[finished_dir[0]] = finished_dir[1]
    elif command[0].isdigit():
        add_size(int(command.split(' ')[0]), current_dirs=current_dirs)
    else:
        pass
    return closed_dirs, current_dirs

def add_size(size, current_dirs):
    for k, v in current_dirs.items():
        current_dirs[k] += size

def get_result(file):
    f = read_file(file)
    closed_dirs, current_dirs = {}, {}
    depth = 0
    for i, command in enumerate(f):
        command = command[:-1]
        if command.startswith('$ cd') and '..' not in command:
            directory = command.split(' ')[2]
            current_dirs[f'{directory}_{i}'] = 0
            depth += 1
            print(f'{command} added new dir', f'{directory}_{i}', len(current_dirs))
        elif command.startswith('$ cd ..'):
            depth -= 1
            finished_dir = current_dirs.popitem()
            print(f'{command} popping last dir: {finished_dir[0]}', len(current_dirs))
            closed_dirs[finished_dir[0]] = finished_dir[1]
        elif command[0].isdigit():
            add_size(int(command.split(' ')[0]), current_dirs=current_dirs)
        else:
            pass
        print(depth)
    closed_dirs.update(current_dirs)
    freed_space = -1*(70000000 - 42536714 - 30000000)
    total_size = 0
    current_smalles_dir_name = ''
    current_smalles_dir_value = float('inf')
    for directory, size in closed_dirs.items():
        if ((int(size) - freed_space) >= 0):
            print(f'change big enough: {size}')
            if int(size) < int(current_smalles_dir_value):
                current_smalles_dir_name = directory
                print(f'changing  current_smallest_dir_value from {current_smalles_dir_value} to {size}')
                current_smalles_dir_value = int(size)
            else:
                print(f'other: {size-current_smalles_dir_value}')
        else:
            print(f'not enough change: {size} -  8381165 = {size -  freed_space}')
    print(current_smalles_dir_value, current_smalles_dir_name)
    closed_dirs = {k: v for k, v in sorted(closed_dirs.items(), key=lambda item: item[1])}
    closed_dirs = {k: v for k, v in closed_dirs.items() if v >= freed_space}
    for directory, size in closed_dirs.items():
        if size < 100000:
            total_size += size

    print(total_size)

def check_depth(file):
    file = read_file(file)
    depth = 0
    for line in file:
        if line.startswith('$ cd ..'):
            depth -= 1
        elif line.startswith('$ cd') and '..' not in line:
            depth += 1
        print(depth)
        if depth < 0:
            print('problem', line)


if __name__ == '__main__':
    check_depth('./data/input_7.txt')
    get_result('./data/input_7.txt')