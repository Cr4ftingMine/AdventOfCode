# Advent of Code 2025 - Tag 3.2

# Find highest 12-pair Number in Sequence of numbers
# No rearrangement of numbers allowed
# Each combination is valid, aslong there is no rearrangement
# Return: Sum of highest 12-pair Numbers
# Example: 
# 987654321111111 -> 987654321111
# 811111111111119 -> 811111111119
# 818181911112111 -> 888911112111


def open_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return [line.strip() for line in lines]

def find_highest_pairs(numbers):
    sum_of_highest_pairs = 0
    len_pair = 12
    for number in numbers:
        remove_cnt = len(number) - len_pair
        stack = []

        for digit in number:
            while remove_cnt > 0 and stack and stack[-1] < digit:
                stack.pop()
                remove_cnt -= 1

            stack.append(digit)
        sum_of_highest_pairs += int(''.join(stack[:len_pair]))
    return sum_of_highest_pairs
        

if __name__ == "__main__":
    #print(f"Numbers are: {open_file("input.txt")}")
    print(f"Sum of highest pairs is: {find_highest_pairs(open_file("input.txt"))}")
