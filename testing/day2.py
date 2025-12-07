def part_1(input):
    input_list = input.split(",")
    input_list[-1] = input_list[-1].replace("\n", "")

    invalid_sum = 0

    for input_range in input_list:
        input_range_list = input_range.split("-")
        first = input_range_list[0]
        last = input_range_list[1]

        for i in range(int(first), int(last) + 1):
            if len(str(i)) % 2 == 0:
                first_half = str(i)[: int(len(str(i)) / 2)]
                second_half = str(i)[int(len(str(i)) / 2) :]

                if first_half == second_half:
                    invalid_sum += i

    return invalid_sum


def part_2(input):
    input_list = input.split(",")
    input_list[-1] = input_list[-1].replace("\n", "")

    invalid_sum = 0

    for input_range in input_list:
        input_range_list = input_range.split("-")
        first = input_range_list[0]
        last = input_range_list[1]

        for i in range(int(first), int(last) + 1):
            for len_factor in range(2, len(str(i)) + 1):
                if len(str(i)) % len_factor == 0:
                    len_divider = int(len(str(i)) / len_factor)
                    num_parts = [
                        str(i)[idx : idx + len_divider]
                        for idx in range(0, len(str(i)), len_divider)
                    ]

                    if len(set(num_parts)) == 1:
                        invalid_sum += i
                        break
    return invalid_sum


if __name__ == "__main__":
    with open("testing/inputs/day2.txt", "r") as f:
        input = f.read()

    res_1 = part_1(input)
    print(f"Part 1 answer = {res_1}")

    res_2 = part_2(input)
    print(f"Part 2 answer = {res_2}")
