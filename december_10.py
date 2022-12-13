from december_2 import read_file
import numpy as np
def addx(value, total_sum):
    total_sum += value
    return  total_sum

def noop():
    pass

def execute_cycle(to_add, time, total_sum):
    time += 1
    return total_sum + to_add


def read_instructions(file):
    with open(file, 'r') as f:
        instructions = f.read().split('\n')
    return instructions

def get_cycle_and_value_from_instruction(instruction):
    if instruction.startswith('noop'):
        return [('Tick', 0)]
    elif instruction.startswith('addx'):
        value = int(instruction.split(' ')[1])
        return [('Tick', 0), ('Tick', value)]

class CRT:
    def __init__(self, position, size, cycle, rows, columns):
        self.grid = np.zeros((columns, rows))
        self.sprite_position = 1
        self.drawn_pixel = position
        self.cycle = cycle
        self.size = size
        self.row_length = columns

    def draw_pixel(self):
        if abs(self.sprite_position - self.drawn_pixel[0]) < 2:
            self.grid[self.drawn_pixel[0], self.drawn_pixel[1]] = 1
            print('drawing\n')
        else:
            print('not drawing\n')

    def move_sprite_position(self, new_position):
        self.sprite_position += new_position
        print(f'position: {self.drawn_pixel}')

    def move(self):
        self.drawn_pixel[0] += 1
        if ((self.cycle) % 40) == 0:
            self.drawn_pixel[1] += 1
            self.drawn_pixel[0] = 0

    def draw_grid(self):
        for y in range(self.grid.shape[1]):
            line = []
            for x in range(self.grid.shape[0]):
                if self.grid[x, y] == 0:
                    line.append('.')
                else:
                    line.append('#')
            print(''.join(line))
def get_result(checkpoints, file):
    instructions = read_instructions(file)
    signal_strength = 0
    x_value = 1
    cycle = 0
    for instruction in instructions:
        ticks = get_cycle_and_value_from_instruction(instruction)
        for t in ticks:
            cycle += 1
            print(f'x_value during cycle {cycle}: {x_value}')
            if checkpoints[0] == cycle:
                strength = checkpoints[0]*x_value
                signal_strength += strength
                print(f'adding strength: {strength} to signal strength: {signal_strength}')
                checkpoints.pop(0)
                if len(checkpoints) == 0:
                    print(signal_strength)
                    return
            x_value += t[1]

            print(f'x after cycle {cycle}: {x_value}')

def get_result2(file):
    crt = CRT([0, 0], 3, 0, 6, 40)
    instructions = read_instructions(file)
    for instruction in instructions:
        ticks = get_cycle_and_value_from_instruction(instruction)
        for t in ticks:
            crt.cycle += 1
            print(f'drawing pixel {crt.drawn_pixel} during {crt.cycle}', f'sprite position: {crt.sprite_position}')
            crt.draw_pixel()

            if t[1] != 0:
                crt.move_sprite_position(t[1])
            crt.move()

    crt.draw_grid()


if __name__ == '__main__':
    checkpoints = [20, 60, 100, 140, 180, 220]
    get_result2('./data/input_10.txt')