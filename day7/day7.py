import sys

def map_int_to_char(x):
    if x == 0:
        return '.'
    if x > 0:
        return '|' 
    if x < 0:
        return '^'
    return x

def solve(input_path):
    with open(input_path,"r") as f:
        input = f.read().splitlines()

    part1_answer = 0
    output_grid  = [[1 if char == "S" else 0 for char in input[0]]]
    visual_grid = [input[0]]
    
    for row in input[1:]:
        cur_row = [-1 if char == '^' else 0 for char in row ]
        for i, char in enumerate (row):
            above_char = output_grid[-1][i]
            if above_char > 0:
                if char == "^":
                    part1_answer += 1
                    cur_row[i - 1] += above_char
                    cur_row[i + 1] += above_char
                else :
                    cur_row[i] += above_char
        output_grid.append(cur_row)
        visual_grid.append(''.join(map_int_to_char(x) for x in cur_row)) 

    part2_answer = sum(i for i in output_grid[-1] if i > 0)
    
    with open('day7/output.txt', 'w') as f:
        f.write('\n'.join(''.join(str(row)) for row in visual_grid))
    
    return part1_answer, part2_answer

if __name__ == '__main__':
    path = sys.argv[1] if len(sys.argv) > 1 else 'day7/actual_input.txt'
    part1, part2 = solve(path)
    print("Part 1 answer:" + str(part1))
    print("Part 2 answer:" + str(part2))

