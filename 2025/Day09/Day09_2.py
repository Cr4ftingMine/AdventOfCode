# Advent of Code 2025 - Tag 9.2

# Given 2D Coordinates, in a x = min() to x = max() and y = min() to y = max() grid
# Find the largest area between 2 Coordinates, that from a rectangle 
# Area must be between two coordinates

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
# .......#XXX#..
# .......X...X..
# ..#XXXX#...X..
# ..X........X..
# ..#XXXXXX#.X..
# .........X.X..
# .........#X#..
# ..............

# ..............
# .......#XXX#..
# .......XXXXX..
# ..OOOOOOOOXX..
# ..OOOOOOOOXX..
# ..OOOOOOOOXX..
# .........XXX..
# .........#X#..
# ..............
# Result: Largest rectangle area is 24 -<> 9,5 and 2,3


def read_input(file_path):
    coordinates = []
    with open(file_path) as f:
        for line in f:
            x, y = map(int, line.strip().split(","))
            coordinates.append((x, y))
    return coordinates


def build_scanlines(poly):
    scan = {}

    n = len(poly)
    for i in range(n):
        x1, y1 = poly[i]
        x2, y2 = poly[(i+1) % n]

        if x1 == x2:
            x = x1
            if y1 > y2: y1, y2 = y2, y1
            for y in range(y1, y2):
                scan.setdefault(y, []).append(x)


    intervals = {}
    for y, xs in scan.items():
        xs = sorted(xs)
        row = []
        for i in range(0, len(xs), 2):
            row.append((xs[i], xs[i+1]))
        intervals[y] = row

    return intervals


def interval_inside(intervals, y, xl, xr):
    if y not in intervals:
        return False
    for a, b in intervals[y]:
        if xl >= a and xr <= b:
            return True
    return False


def largest_rect_part2(poly):
    intervals = build_scanlines(poly)
    best = 0
    n = len(poly)

    for i in range(n):
        x1, y1 = poly[i]
        for j in range(i+1, n):
            x2, y2 = poly[j]
            if x1 == x2 or y1 == y2:
                continue

            xl, xr = sorted((x1, x2))
            yl, yr = sorted((y1, y2))
            valid = True

            for y in range(yl, yr+1):
                if not interval_inside(intervals, y, xl, xr):
                    valid = False
                    break

            if valid:
                area = (xr - xl + 1) * (yr - yl + 1)
                if area > best:
                    best = area

    return best


if __name__ == "__main__":
    coordinate_points = read_input("input.txt")
    print(largest_rect_part2(coordinate_points))


