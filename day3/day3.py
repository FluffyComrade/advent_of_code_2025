import sys

def find_highest_joltage(joltage_bank_list):
    final_joltage = []
    digits = int_to_digits(joltage_bank_list)
    number_max = 10
    final_joltage = find_2_biggest_numbers(digits,number_max)
    return digits_to_int(final_joltage)

def find_2_biggest_numbers (input_number, number_max):
    biggest_digit = 0
    second_biggest_digit = 0
    input_number_copy = input_number
    output_number = []

    for i in input_number:
        if i > biggest_digit and i<=number_max : 
            biggest_digit = i

    output_number.append(biggest_digit)
    idx = input_number.index(biggest_digit)
    input_number= input_number[idx+1:]
    
    for i in input_number:
        if i > second_biggest_digit : 
            second_biggest_digit = i
        
    if second_biggest_digit ==0:
        input_number = input_number_copy
        output_number=[]
        number_max = biggest_digit - 1
        biggest_digit = 0
        output_number = find_2_biggest_numbers(input_number,number_max)
    else:
        output_number.append(second_biggest_digit)
    
    return output_number

def int_to_digits(num):
    digits = []
    while num > 0:
        digits.append(num % 10)
        num //= 10
    digits.reverse()
    return digits

def digits_to_int (digits):
    digits.reverse()
    num = 0
    for index, i in enumerate(digits):
        num = num + (i*(10**index))
    return num

def solve(input_path):
    part1_answer = 0
    part2_answer = None
    with open(input_path, 'r') as file:
        
        actualInputArray = [int(line.strip()) for line in file if line.strip()]

    for i in actualInputArray:
        highestJoltage = find_highest_joltage(i)
        part1_answer = part1_answer + highestJoltage
    
    return part1_answer, part2_answer

if __name__ == '__main__':
    path = sys.argv[1] if len(sys.argv) > 1 else 'day3/actual_input.txt'
    part1, part2 = solve(path)
    print("Part 1 answer:" + str(part1))
    print("Part 2 answer:" + str(part2))