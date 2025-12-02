from pathlib import Path

def parse(path="input.txt"):
    return Path(path).read_text().strip().splitlines()

def part1(lines):
    current_position = 50
    zero_count = 0

    for line in lines:
        direction_string = line[0]
        direction_multiplier = -1 if direction_string == 'L' else 1
        # number of steps as an integer
        clicks = int(line[1:])

        clicks_change = direction_multiplier * clicks

        # update current position
        current_position += clicks_change

        if current_position % 100 == 0:
            zero_count += 1

    return zero_count

def part2(lines):
    current_position = 50
    zero_count = 0

    for line in lines:
        direction_string = line[0]
        direction_multiplier = -1 if direction_string == 'L' else 1
        # number of steps as an integer
        clicks = int(line[1:])

        # Go through each click individually 
        for i in range(clicks):
            current_position += direction_multiplier
            
            # If pointing at zero add 1
            if current_position % 100 == 0:
                zero_count += 1
      

    return zero_count

if __name__ == "__main__":
    data = parse()
    print("part1:", part1(data))
    print("part2:", part2(data))
