# Advent of Code - Tag 5.1

# Check of Id is in given Range
# Given Set of Ranges and Ids, check if Id is in any of the Ranges
# Ranges split by "-" | Ranges and Ids separated by new line once 
# Example:
# 3-5
# 10-14
# 16-20
# 12-18

# 1
# 5
# 8
# 11
# 17
# 32

def open_file(file_path):
    with open(file_path, "r") as file:
        ranges = []
        ids = []
        lines = file.read().strip().split("\n\n")
        range_lines = lines[0].split("\n")
        id_lines = lines[1].split("\n")

        for line in range_lines:
            start, end = map(int, line.split("-"))
            ranges.append((start, end))

        for line in id_lines:
            ids.append(int(line))

    return ranges, ids

def is_id_in_ranges(ranges, ids):
    counter = 0
    for id in ids:
        for r in ranges:
            if r[0] <= id <= r[1]:
                print(f"ID {id} is in range {r}")
                counter += 1
                break
    return counter


if __name__ == "__main__":
    ranges, ids = open_file("input.txt")
    print(is_id_in_ranges(ranges, ids))