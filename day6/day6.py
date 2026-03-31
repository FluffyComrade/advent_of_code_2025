import sys, re

#transpose matrix list and per horizntal line
def solve_part1(input_list):
    worksheet = [list(row) for row in zip(*input_list)]
    worksheet_results = []

    for line in worksheet:
        if '+' in line:
            worksheet_results.append(sum(int(x) for x in line if x!='+'))
        if '*' in line:
            result = 1
            line.remove('*')
            for x in line:
                result *= int(x)
            worksheet_results.append(result)
            
    answer = sum(int(x) for x in worksheet_results)
    return answer

#for part 2 its important to keep note of spaces in input, as it changes order for number.
def parse_matrix(s):
    s = s.replace('\r', '')
    rows = [row for row in s.split('\n') if row.strip()]
    
    # find operator row to determine column boundaries
    op_row = next(r for r in rows if '+' in r or '*' in r)
    positions = [m.start() for m in re.finditer(r'[+*]', op_row)]
    positions.append(len(op_row))  
    
    # slice every row
    matrix = []
    for row in rows:
        chunks = [row[positions[i]:positions[i+1]] for i in range(len(positions)-1)]
        matrix.append(chunks)
    
    return matrix

def solve_part2 (input_matrix):
    #transpose matrix so equations vertical =>horizontal and invert to make strings right-to-left
    worksheet = [[x[::-1] for x in row] for row in zip(*input_matrix)]
    worksheet_cepha = []
    worksheet_cepha_results = []

    #convert strings into final values so numbers are in correct order
    y = 0
    for line in worksheet:
        worksheet_cepha.append([])
        sign_string = ''
        for i in range(len(line[0])):
            temp_string = ''
            for x in line:
                if '+' in x or '*' in x:
                    sign_string = x
                    break
                else:
                    temp_string = temp_string + x[i]
            worksheet_cepha[y].append(temp_string)
        worksheet_cepha[y].insert(0,sign_string)
        y = y + 1

    #regular equation solving
    for line in worksheet_cepha:
        cleaned_line = [x for x in line if x.strip()]
        if any('+' in x for x in cleaned_line):
            no_sign_line = [x for x in cleaned_line if x.strip() and '+' not in x]
            worksheet_cepha_results.append(sum(int(x) for x in no_sign_line))
        if any('*' in x for x in cleaned_line):
            result = 1
            no_sign_line = [x for x in cleaned_line if x.strip() and '*' not in x]
            for y in cleaned_line:
                result *= int(y) if '*' not in y else 1 
            worksheet_cepha_results.append(result)


    answer = sum(int(x) for x in worksheet_cepha_results)
    return answer


def solve (input_path):
    
    test_input_part1 = []
    with open(input_path, 'r') as file:
        for line in file: 
            row_list = []
            clean_line = line.split (' ')
            clean_line = [x for x in clean_line if x != '\n' and x != '']
            row_list = list(clean_line)
            test_input_part1.append(row_list)

    part1_answer = solve_part1(test_input_part1)
    test_input_part2 = parse_matrix(open(input_path).read())
    part2_answer = solve_part2(test_input_part2)

    return part1_answer, part2_answer

if __name__ == '__main__':
    path = sys.argv[1] if len(sys.argv) > 1 else 'day6/actual_input.txt'
    part1, part2 = solve(path)
    print("Part 1 answer:" + str(part1))
    print("Part 2 answer:" + str(part2))