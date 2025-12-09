# Advent of Code 2025 - Tag 8.2


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
        rootX = find(x)
        rootY = find(y)
        if rootX == rootY:
            return False
        
        UF[rootX] = rootY
        return True
    return UF, find, union

def solve_part2(points):
    distances = calculate_distance_3d(points)
    UF, find, union = make_union_find(len(points))
    part1 = None
    connections = 0

    for t, (dist, p1, p2) in enumerate(distances):                    
        if union(p1, p2):
            connections += 1
            if connections == len(points) - 1:
                part2 = points[p1][0] * points[p2][0]
                return part2
            
    return None


if __name__ == "__main__":
    print(solve_part2(read_input("input.txt")))