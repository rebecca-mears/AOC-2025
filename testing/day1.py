from math import ceil, floor


def part_1(input):
    input_string = input.replace("L", "-").replace("R", "")
    input = input_string.split("\n")
    input.pop()

    input_list = list(map(int, input))

    count = 0
    dial = 50

    for input in input_list:
        dial += input

        if dial % 100 == 0:
            count += 1

    return count


def part_2(input):
    input_string = input.replace("L", "-").replace("R", "")
    input = input_string.split("\n")
    input.pop()

    input_list = list(map(int, input))

    count = 0
    dial = 50

    for input in input_list:
        if abs(input) < 100:
            if ((input < 0) & ((ceil(dial / 100)) != (ceil((dial + input) / 100)))) | (
                (input > 0) & ((floor(dial / 100)) != (floor((dial + input) / 100)))
            ):
                count += 1
            elif (dial > 0) & ((dial + input) <= 0):
                count += 1
            elif (dial < 0) & ((dial + input) >= 0):
                count += 1

        else:
            if input > 99:
                first = (ceil(dial / 100) * 100) - dial
            else:
                first = (floor(dial / 100) * 100) - dial

            count += floor((abs(input) - abs(first)) / 100)

            if dial % 100 != 0:
                count += 1

        dial += input

    return count


if __name__ == "__main__":
    with open("testing/inputs/day1.txt", "r") as f:
        input = f.read()

    res_1 = part_1(input)
    print(f"Part 1 answer = {res_1}")

    res_2 = part_2(input)
    print(f"Part 2 answer = {res_2}")
