# Advent of Code 2025 - Tag 8.1
from collections import defaultdict


def read_input(file_path):
    points = []
    with open(file_path, "r") as file:
        for line in file:
            x, y, z = map(int, line.strip().split(","))
            points.append((x, y, z))
    return points

def calculate_distance_3d(points):
    distance = []
    n = len(points)
    for p1 in range(n):
        x1, y1, z1 = points[p1]
        for p2 in range(p1 + 1, n):
            x2, y2, z2 = points[p2]
            dist = (x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2
            distance.append((dist, p1, p2))
    return sorted(distance)

def make_union_find(n):
    UF = list(range(n))

    def find(x):
        if UF[x] != x:
            UF[x] = find(UF[x])
        return UF[x]

    def union(x, y):
        rx = find(x)
        ry = find(y)
        if rx == ry:
            return False
        UF[rx] = ry
        return True

    return UF, find, union


def solve_part1(points):
    distances = calculate_distance_3d(points)
    UF, find, union = make_union_find(len(points))

    for t, (dist, p1, p2) in enumerate(distances):
        if t == 1000:
            sizes = defaultdict(int)
            for i in range(len(points)):
                sizes[find(i)] += 1
            comps = sorted(sizes.values())
            if len(comps) < 3:
                return 0
            return comps[-1] * comps[-2] * comps[-3]
        union(p1, p2)

    sizes = defaultdict(int)
    for i in range(len(points)):
        sizes[find(i)] += 1
    comps = sorted(sizes.values())
    if len(comps) < 3:
        return 0
    return comps[-1] * comps[-2] * comps[-3]


if __name__ == "__main__":
    print(solve_part1(read_input("input.txt")))






