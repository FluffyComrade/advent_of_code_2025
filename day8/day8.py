import sys

def connect_circuits (box_ID,circuit_list): 
    id1, id2 = box_ID.split(',')
    if not circuit_list[0]: 
        circuit_list[0].append(id1) 
        circuit_list[0].append(id2) 
    else:
        matches = [sublist for sublist in circuit_list if id1 in sublist or id2 in sublist]
        if len(matches) == 0:
            circuit_list.append([id1,id2])
        if len(matches) == 1:
            if id1 in matches[0] and not(id2 in matches[0]):
                matches[0].append(id2)
            elif id2 in matches[0]and not(id1 in matches[0]):
                matches[0].append(id1)

        elif len(matches) == 2:
            matches[0].extend(matches[1])  
            circuit_list.remove(matches[1]) 

    return circuit_list

def calculate_distance(cord1,cord2):
    x1, y1, z1 = map(int, cord1.split(','))
    x2, y2, z2 = map(int, cord2.split(','))
    distance = ((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2) ** 0.5
    return distance

def solve(input_path):
    with open(input_path, "r") as f:
        pos_list = f.read().splitlines()

    distances = {}
    circuit_list = [[]]
    part1_answer = 1

    for x, pos_x in enumerate(pos_list):
        for y in range(x + 1, len(pos_list)):
            distances[f"{x},{y}"] = calculate_distance(pos_x, pos_list[y])

    sorted_distances = dict(sorted(distances.items(), key=lambda x: x[1]))
    sorted_keys = list(sorted_distances.keys())  

    for i in range(1000):  
        circuit_list = connect_circuits(sorted_keys[i], circuit_list)

    largest_3 = sorted(circuit_list, key=len, reverse=True)[:3]
    for line in largest_3:
        part1_answer *= len(line)

    i = 0
    while max(len(c) for c in circuit_list) != len(pos_list):
        circuit_list = connect_circuits(sorted_keys[i], circuit_list)
        id1, id2 = sorted_keys[i].split(',')
        last_id1, last_id2 = id1, id2  
        i += 1

    x1, y1, z1 = map(int, pos_list[int(last_id1)].split(','))
    x2, y2, z2 = map(int, pos_list[int(last_id2)].split(','))
    part2_answer = x1 * x2 

    return part1_answer, part2_answer

if __name__ == '__main__':
    path = sys.argv[1] if len(sys.argv) > 1 else 'day8/actual_input.txt'
    part1, part2 = solve(path)
    print("Part 1 answer:" + str(part1))
    print("Part 2 answer:" + str(part2))
