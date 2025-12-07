# Advent of Code - Tag 6.2

# Calculate the sum / product of numbers 
# Operation is defined by last line of row 
# Values to calculate are taken from the columns, but in each index of the value


# Example:
# 123 328  51 64 
# 45 64  387 23 
# 6 98  215 314
# *   +   *   +

# Result: 356 * 24 * 1 ; 8 + 248 + 369 ; 175 * 581 * 32 ; 4 + 431 + 623

# Example: 
# 64
# 23
# 314
# + 
# => 623 + 431 + 4 


def open_file(path):
    with open(path, "r") as f:
        lines = f.read().rstrip("\n").splitlines()

    width = max(len(line) for line in lines)
    lines = [line.ljust(width) for line in lines]

    rows = len(lines)
    cols = width

    problems = []
    current_numbers = []
    current_op = None

    for c in range(cols - 1, -1, -1):
        column_chars = [lines[r][c] for r in range(rows)]

        if all(ch == " " for ch in column_chars):
            if current_numbers:
                problems.append((current_numbers[::-1], current_op))
                current_numbers = []
                current_op = None
            continue

        op_candidate = column_chars[-1]
        if op_candidate in ["+", "*"]:
            current_op = op_candidate
            digit_chars = column_chars[:-1]
        else:
            digit_chars = column_chars

        digits = [ch for ch in digit_chars if ch.isdigit()]
        if digits:
            number = int("".join(digits))
            current_numbers.append(number)

    if current_numbers:
        problems.append((current_numbers[::-1], current_op))

    return problems


def calculate_total(path):
    problems = open_file(path)
    total = 0
    for nums, op in problems:
        if op == "+":
            value = sum(nums)
        elif op == "*":
            value = 1
            for n in nums:
                value *= n
        else:
            raise ValueError(f"Unknown op {op}")
        total += value
    return total

if __name__ == "__main__":
    print(calculate_total("input.txt"))