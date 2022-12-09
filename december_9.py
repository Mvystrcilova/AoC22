

class Head:
    def __init__(self, init_position, moves):
        self.x = init_position[0]
        self.y = init_position[1]
        self.steps = moves
        self.current_dir = moves[0][0]
        self.num_of_steps_left = int(moves[0][1])
        self.done = False

    def get_next_step(self):
        if self.num_of_steps_left > 0:
            self.step_in_dir()
            self.num_of_steps_left -= 1
        else:
            self.steps.pop(0)
            if len(self.steps) > 0:
                self.current_dir = self.steps[0][0]
                self.num_of_steps_left = int(self.steps[0][1]) - 1
                self.step_in_dir()
            else:
                self.done = True

    def step_in_dir(self):
        if self.current_dir == 'R':
            self.x += 1
        elif self.current_dir == 'U':
            self.y += 1
        elif self.current_dir == 'L':
            self.x -=1
        elif self.current_dir == 'D':
            self.y -=1
class Tail:
    def __init__(self, init_position, head, id):
        self.x = init_position[0]
        self.y = init_position[1]
        self.visited_positions = []
        self.head = head
        self.id = id
        self.done = False

    def follow_head(self):
        if self.head.done:
            self.done = True
            print(f'tail {self.id} visited_positions: {len(self.visited_positions)}')
            return

        if (self.x - self.head.x) == -2:
            if self.y > self.head.y:
                self.y -= 1
            elif self.y < self.head.y:
                self.y += 1
            self.x += 1

        elif (self.x - self.head.x) == 2:
            if self.y > self.head.y:
                self.y -= 1
            elif self.y < self.head.y:
                self.y += 1
            self.x -= 1

        elif (self.y - self.head.y) == -2:
            if self.x > self.head.x:
                self.x -= 1
            elif self.x < self.head.x:
                self.x += 1
            self.y += 1

        elif (self.y - self.head.y) == 2:
            if self.x > self.head.x:
                self.x -= 1
            elif self.x < self.head.x:
                self.x += 1
            self.y -= 1

        if not (self.x, self.y) in self.visited_positions:
            self.visited_positions.append((self.x, self.y))

def read_moves(file):
    with open(file, 'r') as f:
        moves = f.read().split('\n')
    moves = [move.split(' ') for move in moves]
    return moves
def get_result(head, tail):
    while not head.done:
        head.get_next_step()
        tail.follow_head()
        print(f'head position: {head.x, head.y}')
        print(f'tail_position: {tail.x, tail.y}')

def get_result_for_part2(head, tails):
    while not head.done:
        head.get_next_step()
        print(f'head position: {head.x, head.y}')
        for tail in tails:
            tail.follow_head()
            print(f'tail {tail.id} in position: {tail.x, tail.y}')



if __name__ == '__main__':
    moves = read_moves('./data/input_9.txt')
    head = Head(init_position=(0,0), moves=moves)
    prev_tail = head
    tails = []
    for i in range(1, 10):
        tail = Tail(init_position=(0,0), head=prev_tail, id=i)
        prev_tail = tail
        tails.append(tail)

    get_result_for_part2(head, tails)


