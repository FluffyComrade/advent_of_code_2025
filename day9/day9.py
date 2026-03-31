import sys

def createRec (cord1,cord2):
    x1, y1 = cord1[0], cord1[1]
    x2, y2 = cord2[0], cord2[1]
    area = (abs(x2-x1)+1)*(abs(y2-y1)+1)
    return area

def solve (input_path):
    test_input = []
    area_list = []

    with open(input_path, 'r') as file:
        for line in file: 
            clean_line = line.strip().split(',')
            row_list = list(clean_line)
            test_input.append(row_list)

    test_input = [[int(x) for x in sublist] for sublist in test_input]

    for pos1 in test_input:
        for pos2 in test_input:
            area_list.append(createRec(pos1,pos2))
    
    part1_answer = max(area_list)
    part2_answer = None
    return part1_answer, part2_answer

if __name__ == '__main__':
    path = sys.argv[1] if len(sys.argv) > 1 else 'day9/actual_input.txt'
    part1, part2 = solve(path)
    print("Part 1 answer:" + str(part1))
    print("Part 2 answer:" + str(part2))
