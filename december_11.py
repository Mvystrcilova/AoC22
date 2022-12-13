import math
import time
class Monkey:
    def __init__(self, id, items, operation, divisor, modulo):
        self.id = id
        self.items = items
        self.current_item = None
        self.operation = operation
        # self.worry_increase = worry_increase
        self.divisor = divisor
        self.true_monkey = None
        # self.divisibility_test = divisibility_test
        self.false_monkey = None
        self.inspection_count = 0
        self.modulo = modulo

    def increase_worry(self):
        old = self.current_item
        new = eval(self.operation)
        return new

    def check_divisibitily(self, worry):
        divisible = not (worry % self.divisor)
        # worry = worry % 23

        return divisible, worry

    def throw_item(self, worry):
        divisible, worry = self.check_divisibitily(worry)
        if divisible:

            self.true_monkey.items.append(worry)
            # print(f'throwing {worry} to monkey {self.true_monkey.id}')
        else:
            self.false_monkey.items.append(worry)
            # print(f'throwing {worry} to monkey {self.false_monkey.id}')


    def test_divisibility(self, number):
        return self.divisibility_test(number)

    def play_turn(self):
        print(f'monkey {self.id} playing')
        while len(self.items) > 0:
            # print(f'starting with item: {self.items[0]}')
            self.current_item = int(self.items[0])
            self.items.pop(0)
            self.inspection_count += 1
            worry = self.increase_worry()
            worry = worry%self.modulo
            # worry = int(math.floor(worry))
            self.throw_item(worry)

def read_input(monkey_info):
    monkeys = {}
    modulo = 1
    for monkey in monkey_info:
        monkey = monkey.split('\n')
        id = monkey[0].split(' ')[1][:-1]
        items = monkey[1].replace(',', '').split(' ')[4:]
        operation = monkey[2].replace('Operation: new = ', '')
        # if id == '2':
        #     operation = 'pow(old, 2)'
        divisor = int(monkey[3].split(' ')[-1])
        modulo *= divisor
        print(divisor, modulo)
        true_monkey = monkey[4].split(' ')[-1]
        false_monkey = monkey[5].split(' ')[-1]
        new_monkey = Monkey(id=id, items=items, operation=operation, divisor=divisor, modulo=None)
        monkeys[id] = (new_monkey, true_monkey, false_monkey)

    completed_monkeys = []
    for id, throwing_partners in monkeys.items():
        throwing_partners[0].true_monkey = monkeys[throwing_partners[1]][0]
        throwing_partners[0].false_monkey = monkeys[throwing_partners[2]][0]
        completed_monkeys.append(throwing_partners[0])
        throwing_partners[0].modulo = modulo
    return completed_monkeys


def read_file(file):
    with open(file, 'r') as f:
        monkey_info =  f.read().split('\n\n')
    return monkey_info

def get_result(file):
    monkey_info = read_file(file)
    monkeys = read_input(monkey_info)
    for round in range(10000):
        print(round)
        for monkey in monkeys:
            monkey.play_turn()

    monkeys.sort(key=lambda x: x.inspection_count, reverse=True)

    print(monkeys[0].inspection_count * monkeys[1].inspection_count)
if __name__ == '__main__':
    get_result('./data/input_11.txt')