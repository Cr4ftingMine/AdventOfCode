# Advent of Code - Tag 5.2

# Get Ids out of Ranges
# Given Set of Ranges and extract ids out of ranges
# Ranges can overlap
# Ranges split by "-" | Ranges
# Example:
# 3-5
# 10-14
# 16-20
# 12-18
# Extracted Ids: 3,4,5,10,11,12,13,14,16,17,18,19,20

def open_file(file_path):
    with open(file_path, "r") as file:
        ranges = []
        lines = file.read().strip().split("\n\n")
        range_lines = lines[0].split("\n")

        for line in range_lines:
            start, end = map(int, line.split("-"))
            ranges.append((start, end))

    return ranges

def get_ids_from_ranges_faster(ranges):
    ranges = sorted(ranges)
    merged_ranges = []
    current_start, current_end = ranges[0]

    for start, end in ranges[1:]:
        if start > current_end + 1:
            merged_ranges.append((current_start, current_end))
            current_start, current_end = start, end
        else:
            current_end = max(current_end, end)

    merged_ranges.append((current_start, current_end))

    return sum(end - start + 1 for start, end in merged_ranges)



if __name__ == "__main__":
    ranges = open_file("input.txt")
    print(get_ids_from_ranges_faster(ranges))