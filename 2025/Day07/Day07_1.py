# Advent of Code - Tag 7.1

# Calculate total of beams in a structure based on input data
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

# Result: 21 Splits
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

    beams = set()
    visited = set()
    count = 0

    for y in range(height):
        for x in range(width):
            if lines[y][x] == "S":
                beams.add((x, y + 1))
                break

    while beams:
        new_beams = set()

        for x, y in beams:

            if not (0 <= x < width and 0 <= y < height):
                continue

            if (x, y) in visited:
                continue
            visited.add((x, y))

            cell = lines[y][x]

            if cell == ".":
                new_beams.add((x, y + 1))

            elif cell == "^":
                count += 1
                new_beams.add((x - 1, y + 1))
                new_beams.add((x + 1, y + 1))

        beams = new_beams

    return count


if __name__ == "__main__":
    print(process_structure(read_input("input.txt")))