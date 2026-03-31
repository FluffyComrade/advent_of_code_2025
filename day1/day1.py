import sys

def solve(input_path):
    part1_answer = 0
    part2_answer = 0
    cur_pos = 50
    
    with open(input_path, 'r') as file:
        for line in file:
            direction = line[0]
            distance = int(line[1:])
            #for more than 1 circles made
            part2_answer += distance//100
            distance = distance % 100
            if direction == 'L':
                distance = distance*(-1)
            #turned a circle or not 
            if cur_pos+distance >= 100 or cur_pos+distance <= 0:
                # prevent double count
                if cur_pos != 0:
                    part2_answer+=1
            cur_pos += distance
            cur_pos %= 100
            if cur_pos == 0:
                part1_answer += 1
    
    return part1_answer, part2_answer

if __name__ == '__main__':
    path = sys.argv[1] if len(sys.argv) > 1 else 'day1/actual_input.txt'
    part1, part2 = solve(path)
    print("Part 1 answer:" + str(part1))
    print("Part 2 answer:" + str(part2))



