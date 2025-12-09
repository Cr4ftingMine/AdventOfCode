import pprint
# Advent of Code 2025 - Tag 9.1

# Given 2D Coordinates, in a x = min() to x = max() and y = min() to y = max() grid
# Find the largest area between 2 Coordinates, that from a rectangle 

# Example:
# 7,1
# 11,1
# 11,7
# 9,7
# 9,5
# 2,5
# 2,3
# 7,3

# ..............
# ..OOOOOOOOOO..
# ..OOOOOOOOOO..
# ..OOOOOOOOOO..
# ..OOOOOOOOOO..
# ..OOOOOOOOOO..
# ..............
# .........#.#..
# ..............
# Result: Largest rectangle area is 50 -> 2,5 to 11,1 


def read_input(file_path):
    coordinates = []
    with open(file_path, "r") as file:
        for line in file:
            x, y = map(int, line.strip().split(","))
            coordinates.append((x, y))
    return coordinates


def process_grid(coordinates):
    largest_area = 0
    n = len(coordinates)
    for i in range(n):
        for j in range(i + 1, n):
            x1, y1 = coordinates[i]
            x2, y2 = coordinates[j]
            if x1 != x2 and y1 != y2: 
                area = (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1)
                if area > largest_area:
                    largest_area = area
    return largest_area

if __name__ == "__main__":

    print(process_grid(read_input("input.txt")))