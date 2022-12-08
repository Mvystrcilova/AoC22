from collections import Counter


def read_file_to_string(file):
    with open(file, 'r') as f:
        code = f.read().replace('\n', '')
    return code


def get_result(file, window_size=4):
    code = read_file_to_string(file)
    # code = 'mjqjpqmgbljsphdztnvjfqwrcgsmlb'
    for i in range(len(code)):
        counts = Counter(code[i:i+window_size])
        if max(counts.values()) == 1:
            print(code[i:i+window_size], counts, i+window_size)


if __name__ == '__main__':
    get_result('./data/input_6.txt', window_size=14)