from collections import deque#
import pulp
# Advent of Code 2025 - Tag 10.1 

# Find fewest Buttonspresses to reach the target state of lights
# [ ] -> Wanted State (. = off, # = on)
# ( ) -> Button (press toggles the lights inside the brackets)
# { } -> Joltage Requirements (?)

# Example Input:
# [.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7} 

# Fewest Buttonspresses to reach target state and joltage requirements -> 10 button presses


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


def solve_part2(target, buttons):
    dim = len(target)
    num_buttons = len(buttons)

    prob = pulp.LpProblem("JoltageSolver", pulp.LpMinimize)

    x = [pulp.LpVariable(f"x_{j}", lowBound=0, cat="Integer") for j in range(num_buttons)]

    prob += pulp.lpSum(x)

    for counter in range(dim):
        prob += (
            pulp.lpSum(x[j] for j in range(num_buttons) if counter in buttons[j]) 
            == target[counter]
        )

    prob.solve(pulp.PULP_CBC_CMD(msg=False))

    if pulp.LpStatus[prob.status] != "Optimal":
        return None

    return sum(v.value() for v in x)


def process_input(data):
    results = []
    for target_state, button_list, joltage_req in data:
        presses = solve_part2(joltage_req, button_list)
        if presses is None:
            raise ValueError("No solution found for machine with joltage target " + str(joltage_req))
        results.append(presses)
    return sum(results)



if __name__ == "__main__":
    print(process_input(read_input("input.txt")))