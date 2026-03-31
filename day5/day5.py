import sys

def read_input_data (input_path):
    ID_range_list = []
    available_ID_list = []
    has_reached_space = False

    with open(input_path, 'r') as file:
        for line in file:
            clean_line = line.strip() 
            if not has_reached_space and clean_line == '':
                has_reached_space = True
                continue
            if not has_reached_space:
                range = clean_line.split('-')
                num_range = []
                num_range.append(int(range[0]))
                num_range.append(int(range[1]))
                ID_range_list.append(num_range)
            if has_reached_space:
                available_ID_list.append(int(clean_line))
                
    return ID_range_list, available_ID_list
    
def is_in_range (value, min, max):
    if value>=min and value<=max:
        return True
    else: 
        return False
            
def solve(input_path):
    part1_answer = 0
    part2_answer = 0

    fresh_ID_range, available_ID= read_input_data(input_path)

    #part 1: every number is compared if it falls within range
    for ID in available_ID:
        for range in fresh_ID_range:
            if is_in_range(ID,range[0],range[1]):
                part1_answer+=1
                break
    
    #part 2: 
    #looping through all numbers like in part 1 is impractical, so for part 2 sort list and check if we can merge ranges
    fresh_ID_range.sort(key=lambda x: x[0])
    merged = [fresh_ID_range[0]]

    for r in fresh_ID_range[1:]:
        last = merged[-1]
        if r[0] <= last[1]:          
            last[1] = max(last[1], r[1])  
        else:
            merged.append(r)         
    for range in merged:
        part2_answer = part2_answer + range[1]-range[0] + 1

    return part1_answer, part2_answer

if __name__ == '__main__':
    path = sys.argv[1] if len(sys.argv) > 1 else 'day5/actual_input.txt'
    part1, part2 = solve(path)
    print("Part 1 answer:" + str(part1))
    print("Part 2 answer:" + str(part2))