# Advent of Code 2025 - Tag 1.2

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
        
        # Volle Umdrehungen
        steps = abs(value)
        full_rotation = steps // max
        count_on_zero += full_rotation

        rest_clicks = steps % max

        # Restliche Klicks + Crossing check
        moved_over = False
        if direction == "R": # Drehung nach rechts
            dist_to_zero = (max - start) % max
            if dist_to_zero != 0 and dist_to_zero <= rest_clicks:
                moved_over = True
        
        else: # Drehung nach links
            dist_to_zero = start % max
            if dist_to_zero != 0 and dist_to_zero <= rest_clicks:
                moved_over = True
        
        # Endposition
        new_start = (start + value) % max
        if new_start == 0:
            end_hit = True
        else:
            end_hit = False

        # Treffer zählen
        if end_hit:
            count_on_zero += 1
        elif moved_over:
            count_on_zero += 1

        start = new_start
    return count_on_zero


if __name__ == "__main__":
    operation = (open_file("input.txt"))
    result = process_operations(operation)
    print("Anzahl der 0-Positionen:", result)