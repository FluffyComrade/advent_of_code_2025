import sys
import re
from collections import deque

def pressButton (light,button):
    light = list(light)
    for item in button:
        light[int(item)] = not light[int(item)]
    light = tuple(light)
    return light

def bfs(start, goal, get_buttons):
    start = tuple(start) 
    goal = tuple(goal) 
    queue = deque([(start, [])]) 
    visited = {start}
    step = 0
    while queue:
        state, moves = queue.popleft()
        if state == goal:
            return moves      
             
        for i, button in enumerate(get_buttons):
            new_state = list(state)
            btn  = tuple(button) 
            new_state = pressButton(new_state,btn)
                
            if new_state not in visited:
                visited.add(new_state)
                queue.append((new_state, moves + [i]))


def solve (input_path):
    lights_task = []
    buttons = []
    path_lists = []
    mapping = {'.': False, '#': True}

    with open(input_path, 'r') as file:

        for line in file: 
            square = re.findall(r'\[([^\]]*)\]', line)
            lights_task.append([list(x for x in g.split(',')) if ',' in g else g for g in square]) 
            regular = re.findall(r'\(([^)]*)\)', line)
            buttons.append([
        list(int(x) for x in g.split(',')) if ',' in g else [int(g)]for g in regular])
    
    lights_task = [[mapping[char] for char in line[0]] for line in lights_task]

    for i,task in enumerate(lights_task):
        startLights = [False] * len(task)
        path_lists.append(bfs(startLights,task,buttons[i]))

    part1_answer = 0

    for path in path_lists:
        part1_answer += + len(path)

    part2_answer = None

    return part1_answer, part2_answer

if __name__ == '__main__':
    path = sys.argv[1] if len(sys.argv) > 1 else 'day10/actual_input.txt'
    part1, part2 = solve(path)
    print("Part 1 answer:" + str(part1))
    print("Part 2 answer:" + str(part2))
