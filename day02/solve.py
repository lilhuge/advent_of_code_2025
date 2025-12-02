from pathlib import Path

def parse(path="input.txt"):
    return Path(path).read_text().strip().split(",")

def part1(number_sets):
    
    invalid_sum = 0
    for number_set in number_sets:

        start, end = map(int, number_set.split("-"))

        for number in range(start, end + 1):
            num_str = str(number)

            # If odd skip
            if len(num_str) % 2 != 0:
                continue
            half_length = len(num_str) // 2

            first_half = int(num_str[: half_length])
            second_half = int(num_str[half_length :])

            if first_half == second_half:
                invalid_sum += number
                

    return invalid_sum

def part2(number_sets):

    invalid_sum = 0
    for number_set in number_sets:
        
        start, end = map(int, number_set.split("-"))

        for number in range(start, end + 1):

            num_str = str(number)

            string_len = len(num_str)

            
            # Get the largest integer repeatable pattern for the string length
            longest_repeatable_length = len(num_str) // 2


            for pattern_len in range(1, longest_repeatable_length +1):
                # If string length isn't divisible by pattern length, skip 
                if string_len % pattern_len !=0:
                    continue

                # Split the sting into even chunks of length = pattern_len
                pattern_chunks = [num_str[i:i + pattern_len] for i in range(0, string_len, pattern_len)]

                all_chunks_equal = len(set(pattern_chunks)) == 1

                if all_chunks_equal:
                    invalid_sum += number
                    # If matched for a given pattern length, break so we don't count more than once
                    break



    return invalid_sum

if __name__ == "__main__":
    data = parse()
    print("part1:", part1(data))
    print("part2:", part2(data))
