# Advent of Code 2025 - Tag 1.1

# Einlesen aus input.txt
def open_file(path):
    operation = []
    with open(path) as f:
        start = 50
        for line in f:
            string = line.strip()
            operation.append(string)
    return operation

# Verarbeitung der Operationen
def process_operations(operations):
    start = 50
    max = 100
    count_on_zero = 0
    for op in operations:
        direction = op[0]
        value = int(op[1:])
        if direction == 'L':
            value = value * -1
        elif direction == 'R':
            value = value
        start = (start + value) % max
        if start == 0: 
            count_on_zero += 1
    return count_on_zero


if __name__ == "__main__":
    operation = (open_file("input.txt"))
    result = process_operations(operation)
    print("Anzahl der 0-Positionen:", result)


