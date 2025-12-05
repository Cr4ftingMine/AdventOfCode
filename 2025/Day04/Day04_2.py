# Advent of Code - Tag 4.2

# Check if Rolls (@) can be moved -> Movable if there are not more than 4 Rolls in the 8 adjacent cells (horizontally, vertically, diagonally)
# If movable, count++ 
# Initial rolls will be removed and process repeated until no more rolls can be moved
# Example:
# ..@@.@@@@.
# @@@.@.@.@@
# @@@@@.@.@@
# @.@@@@..@.
# @@.@@@@.@@
# .@@@@@@@.@
# .@.@.@.@@@
# @.@@@.@@@@
# .@@@@@@@@.
# @.@.@@@.@.
# 13 Rolls can be moved 


# Positions: [Vertikal][Horizontal]
# -1 | -1       -1 | 0      -1 | 1
#  0 | -1        0 | 0       0 | 1
#  1 | -1        1 | 0       1 | 1

positions = [(-1, -1), (-1, 0), (-1, 1),
             (0, -1),           (0, 1),
             (1, -1),  (1, 0),  (1, 1)]

def open_file(file_path):
    with open(file_path, 'r') as file:
        grid = [list(line.strip()) for line in file.readlines()]
    return grid


def process_lines(grid):
    movable_count = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "@":
                count = 0
                for pos in positions:
                    n_i, n_j = i + pos[0], j + pos[1]
                    if 0 <= n_i < len(grid) and 0 <= n_j < len(grid[i]):
                        if grid[n_i][n_j] == "@":
                            count += 1
                if count < 4:
                    movable_count += 1
                    grid[i][j] = "."  # Remove the moved roll
    return movable_count 

def repeat_until_no_moves(grid):
    total_moved = 0
    while True:
        moved = process_lines(grid)
        if moved == 0:
            break
        total_moved += moved
    return total_moved


if __name__ == "__main__":
    print(repeat_until_no_moves(open_file("input.txt")))