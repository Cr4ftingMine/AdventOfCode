# Advent of Code - Tag 6.1

# Calculate the sum / product of numbers 
# Operation is defined by last line of row 


# Example:
# 123 328  51 64 
# 45 64  387 23 
# 6 98  215 314
# *   +   *   +

# Result: 123 * 45 * 6 ; 328 + 64 + 98 ;  51 * 387 * 215 ; 64 + 23 + 314


def open_file(file_path):
    numbers_array = []
    operations_array = []
    with open(file_path, 'r') as file:
        lines = file.read().strip().splitlines()

    for line in lines[:-1]:
        numbers = list(map(int, line.split()))
        numbers_array.append(numbers)
    
    operations_array = lines[-1].split()
    return numbers_array, operations_array

def calculate_result(numbers_array, operations_array):
    result = 0

    columns = list(zip(*numbers_array))
    for columns_values, operation in zip(columns, operations_array):
        if operation == '+':
            result += sum(columns_values)
        elif operation == '*':
            product = 1
            for num in columns_values:
                product *= num
            result += product

    return result

if __name__ == "__main__":
    numbers_array, operations_array = open_file('input.txt')
    print(calculate_result(numbers_array, operations_array))