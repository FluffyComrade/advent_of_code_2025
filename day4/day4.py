import sys

#counts surrounding 8 tiles in matrix for presence of '@' 
def count_possible_x (input_matrix, row, col):
    x_count = 0
    currentRow = input_matrix[row]

    #prevent checks on top and bottom row because list looping indexes
    if row == 0:
        previousRow = []
    else: 
        previousRow = input_matrix[row-1]
    if row == len(input_matrix)-1:
        nextRow = []
    else:
        nextRow = input_matrix[row+1]
    
    #same row
    if safe_get(currentRow, col-1) == '@':
        x_count += 1
    if safe_get(currentRow, col+1) == '@':
        x_count += 1

    #row above    
    if safe_get(nextRow, col) == '@':
        x_count += 1
    if safe_get(nextRow, col-1) == '@':
        x_count += 1
    if safe_get(nextRow, col+1) == '@':
        x_count += 1
    
    #row below
    if safe_get(previousRow, col) == '@':
        x_count += 1
    if safe_get(previousRow, col-1) == '@':
        x_count += 1
    if safe_get(previousRow, col+1) == '@':
        x_count += 1
    
    return x_count

def safe_get (input_list,index,default=None):
    try:
        if index < 0 or index >= len(input_list):
            return default
        else:
            return input_list[index]
    except IndexError:
        return default

#recreate the grid and replace available rolls with x
def solve_part1(input_grid):
    answer = 0
    answer_list = [[col for col in range(0)] for row in range(len(input_grid))]
    
    for x in range(0,len(input_grid)):
        for y in range(0,len(input_grid[0])):
            if input_grid[x][y]=='@':
                if count_possible_x(input_grid,x,y) < 4 :
                    answer = answer + 1
                    answer_list[x].insert(y,'x')
                else:
                    answer_list[x].insert(y,'@')
            else: 
                answer_list[x].insert(y,'.')
    
    return answer, answer_list

#iteratively recreate the grid, stops when no changes were made in previous iteration 
def solve_part2(input_grid):
    answer = 0
    answer_list = [[col for col in range(0)] for row in range(len(input_grid))]
    previous_list=input_grid
    counter = 0

    while answer_list != previous_list:
        if counter >0:
            previous_list = answer_list
            answer_list = [[col for col in range(0)] for row in range(len(input_grid))]

        for x in range(0,len(previous_list)):
            for y in range(0,len(previous_list[0])):
                if previous_list[x][y]=='@':
                    if count_possible_x(previous_list,x,y) < 4 :
                        answer = answer + 1
                        answer_list[x].insert(y,'x')
                    else:
                        answer_list[x].insert(y,'@')
                elif previous_list[x][y]=='x':
                    answer_list[x].insert(y,'.')
                else: 
                    answer_list[x].insert(y,'.')
        counter = counter + 1
    return answer, answer_list
                
def solve(input_path):
    test_input = []

    with open(input_path, 'r') as file:
        for line in file: 
            row = []
            clean_line = line.strip()
            row = list(clean_line)
            test_input.append(row)

    part1_answer,part1_answer_list = solve_part1(test_input)
    part2_answer,part2_answer_list = solve_part2(test_input)
    
    return part1_answer, part2_answer

if __name__ == '__main__':
    path = sys.argv[1] if len(sys.argv) > 1 else 'day4/actual_input.txt'
    part1, part2 = solve(path)
    print("Part 1 answer:" + str(part1))
    print("Part 2 answer:" + str(part2))

