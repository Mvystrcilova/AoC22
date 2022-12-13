from december_11 import read_file
import ast
import copy

class PackageList:
    def __init__(self, lists, dp1, dp2, dp1_pos, dp2_pos):
        self.lists = lists
        self.dp1 = dp1
        self.dp2 = dp2
        self.dp1_position = dp1_pos
        self.dp2_position = dp2_pos
        self.change = True


    def compare_two(self, left, right, index):
        result = compare_lists(copy.deepcopy(left), copy.deepcopy(right))
        if result != 1:
            self.lists[index] = right
            self.lists[index+1] = left

            if left == self.dp1:
                self.dp1_position = index+1
            elif left == self.dp2:
                self.dp2_position = index + 1

            if right == self.dp1:
                self.dp1_position = index
            elif right == self.dp2:
                self.dp2_position = index
            return True
        return False

    def get_divider_packet_indices(self):
        print(self.dp1_position+1, self.dp2_position+1)
        print((self.dp1_position+1)*(self.dp2_position+1))

    def order_list(self):
        while self.change:
            self.change = False
            for i in range(1,len(self.lists)):
                change = self.compare_two(left = self.lists[i-1], right=self.lists[i], index=i-1)
                if change:
                    self.change=change



def compare_lists(left, right):
    print(f'comparing {left} and {right}')
    if (len(right) == 0)  and (len(left) != 0):
        return -1
    elif (len(left)) == 0 and (len(right) != 0):
        return 1
    elif (len(left) == 0) and (len(right) == 0):
        return 0

    else:
        left_item = left.pop(0)
        right_item = right.pop(0)
        print(f'comparing {left_item} and {right_item}')

        if isinstance(left_item, int) and isinstance(right_item,int):
            if left_item == right_item:
                return compare_lists(left, right)
            elif left_item < right_item:
                return 1
            else:
                return -1
        else:
            if not isinstance(left_item, list):
                left_item = [left_item]
            if not isinstance(right_item, list):
                right_item = [right_item]
            sublist_comparison = compare_lists(left_item, right_item)
            if sublist_comparison == 0:
                return compare_lists(left, right)
            else:
                return sublist_comparison



def read_list(pair, divisor_pair1, divisor_pair2):
    index = -1
    if pair == divisor_pair1:
        index = 1
    if pair == divisor_pair2:
        index = 2
    return ast.literal_eval(pair), index
    # right = ast.literal_eval(pair[1])
    # return left, right

def get_lists(file):
    packets = []
    with open(file, 'r') as f:
        lines =  f.read().split('\n')
        for line in lines:
            if line != '':
                packets.append(line)
    return packets
def get_result(file):
    packets = get_lists(file)
    all_packets = {}
    dp1_index = None
    dp2_index = None
    for i, packet in enumerate(packets):
        packet, index = read_list(packet, '[[2]]', '[[6]]')
        if index != -1:
            if index == 1:
                dp1_index = i
            elif index == 2:
                dp2_index = i
        all_packets[i] = packet

    package_list = PackageList(all_packets, all_packets[dp1_index], all_packets[dp2_index], dp1_index, dp2_index)
    package_list.order_list()
    package_list.get_divider_packet_indices()


if __name__ == '__main__':
    get_result('data/input_13.txt')

