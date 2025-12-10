from collections import deque
# Advent of Code 2025 - Tag 10.1 

# Find fewest Buttonspresses to reach the target state of lights
# [ ] -> Wanted State (. = off, # = on)
# ( ) -> Button (press toggles the lights inside the brackets)
# { } -> Joltage Requirements (?)

# Example Input:
# [.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7} 

# Fewest Buttonspresses to reach target state: 2 -> Pressing (0,2) and (0,1) each once 


def read_input(file_path):
    parsed_lines = []
    with open(file_path, "r") as file:
        for line in file:
            line = line.strip()
            target_state, button_list, joltage_req = parse_line(line)
            parsed_lines.append((target_state, button_list, joltage_req))

    return parsed_lines

def parse_line(line):
    start = line.index('[') + 1
    end = line.index(']')

    target_state = [1 if c == "#" else 0 for c in line[start:end]]

    mid = line[end+1 : line.index("{")].strip()

    buttons = []
    for part in mid.split():
        if part.startswith("(") and part.endswith(")"):
            inside = part[1:-1]
            if inside == "":
                buttons.append([])
            else:
                buttons.append([int(x) for x in inside.split(",")])

    start = line.index("{") + 1
    end = line.index("}")
    joltage_reqs = [int(x) for x in line[start:end].split(",")]

    return target_state, buttons, joltage_reqs


def to_bitmask(button, num_lights):
    bitmask = 0
    for b in button:
        bitmask |= (1 << b)
    return bitmask

def list_to_bitmask(state_list):
    bitmask = 0
    for i, v in enumerate(state_list):
        if v == 1:
            bitmask |= (1 << i)
    return bitmask

def min_presses(target_state, button_list):
    num_lights = len(target_state)

    target_mask = list_to_bitmask(target_state)
    button_masks = [to_bitmask(button, num_lights) for button in button_list]

    queue = deque([(0, 0)])  # (current_state, presses)
    visited = {0}

    while queue:
        state, steps = queue.popleft()

        if state == target_mask:
            return steps
        
        for button_mask in button_masks:
            new_state = state ^ button_mask
            if new_state not in visited:
                visited.add(new_state)
                queue.append((new_state, steps + 1))
    return None

def process_input(data):
    results = []
    for target_state, button_list, joltage_req in data:
        presses = min_presses(target_state, button_list)
        results.append(presses)
    return sum(results)


if __name__ == "__main__":
    print(process_input(read_input("input.txt")))