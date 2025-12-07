from collections import defaultdict
# Advent of Code - Tag 7.2

# Calculate the count of different beams of a single beam (tachyon)
# S = Start of beam
# ^ = Beam Segment -> Split into two beams left and right 
# Beams travel down until they hit a split or the end 

# Example: 
# .......S.......
# ...............
# .......^.......
# ...............
# ......^.^......
# ...............
# .....^.^.^.....
# ...............
# ....^.^...^....
# ...............
# ...^.^...^.^...
# ...............
# ..^...^.....^..
# ...............
# .^.^.^.^.^...^.
# ...............

# Result: 40 Beams
# .......S.......
# .......|.......
# ......|^|......
# ......|.|......
# .....|^|^|.....
# .....|.|.|.....
# ....|^|^|^|....
# ....|.|.|.|....
# ...|^|^|||^|...
# ...|.|.|||.|...
# ..|^|^|||^|^|..
# ..|.|.|||.|.|..
# .|^|||^||.||^|.
# .|.|||.||.||.|.
# |^|^|^|^|^|||^|
# |.|.|.|.|.|||.|


def read_input(file_path):
    with open(file_path, "r") as file:
        return [line.rstrip('\n') for line in file.readlines()]

def process_structure(lines):
    height = len(lines)
    width = len(lines[0])

    beams = defaultdict(int)

    for y in range(height):
        for x in range(width):
            if lines[y][x] == "S":
                beams[(x, y+1)] = 1
                break
    total = 0

    while beams:
        new_beams = defaultdict(int)

        for (x, y), count in beams.items():
            if not (0 <= x < width and 0 <= y < height):
                total += count
                continue

            cell = lines[y][x]

            if cell == ".":
                new_beams[(x, y+1)] += count
            elif cell == "^":
                if x-1 < 0:
                    total += count
                else:
                    new_beams[(x-1, y+1)] += count
                if x+1 >= width:
                    total += count
                else:
                    new_beams[(x+1, y+1)] += count
            else:
                new_beams[(x, y+1)] += count
        beams = new_beams
    return total

if __name__ == "__main__":
    print(process_structure(read_input("input.txt")))