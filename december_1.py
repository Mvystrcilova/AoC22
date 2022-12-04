# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def get_result(txt_file):
    f = open(txt_file)
    sums = []
    current_sum = 0
    for line in f:
        if len(line) > 1:
            current_sum += int(line[:-1])
        else:
            sums.append(current_sum)
            current_sum = 0
    print(max(sums))
    print(sum(sorted(sums)[::-1][:3]))
    # Use a breakpoint in the code line below to debug your script.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(get_result('./data/input.txt'))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
