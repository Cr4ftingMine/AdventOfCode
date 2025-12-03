# Advent of Code 2025 - Tag 2.2

# Invalid IDs: (Presented in Startnumber to Endnumber, e.g. 11-12)
# Leading zeros 
# Sequence of digits repeated twice (e.g. 55, 6464, 123123)
# Some Sequence of digits repeated atleast twice (e.g. 12341234 (1234 two times), 123123123 (123 three times),
#  1212121212 (12 five times), 11111111 (1 eight times))

# Add up invalid IDs for final result


# Read input
def open_file(path):
    ranges = []
    with open(path) as f:
        for line in f:
            parts = [p.strip() for p in line.split(',') if p.strip()]
            ranges.extend(parts)
    return ranges

# Check for invalid IDs
def check_invalid_ids(ranges):
    invalidIdSum = 0
    for r in ranges:
        start, end = map(int, r.split('-'))
        for id in range(start, end + 1):
            id_str = str(id)
            if has_leading_zero(id_str):
                invalidIdSum += id
            elif is_repeated_sequence(id_str):
                invalidIdSum += id

    return invalidIdSum

# Check for leading zero
def has_leading_zero(id_str):
    return id_str[0] == '0'

# Check for repeated sequence
def is_repeated_sequence(id_str):
    length = len(id_str)
    for sub_len in range(1, length // 2 + 1):
        if length % sub_len == 0:
            sub_str = id_str[:sub_len]
            if sub_str * (length // sub_len) == id_str:
                return True
    return False


if __name__ == "__main__":
    ranges = open_file("input.txt")
    print(check_invalid_ids(ranges))