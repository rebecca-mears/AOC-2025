def part_1(input):
    input_list = input.split("\n")
    input_list.pop()

    total_joltage = 0

    for bank in input_list:
        first_digit = max(bank[:-1])
        bank_remaining = bank.split(first_digit, 1)[1]

        second_digit = max(bank_remaining)

        joltage = int(first_digit + second_digit)
        total_joltage += joltage

    return total_joltage


def part_2(input):
    input_list = input.split("\n")
    input_list.pop()

    total_joltage = 0

    for bank_remaining in input_list:
        digit_list = []

        for i in range(11, 0, -1):
            digit = max(bank_remaining[:-i])

            digit_list.append(digit)
            bank_remaining = bank_remaining.split(digit, 1)[1]

        digit_list.append(max(bank_remaining))

        joltage = int("".join(digit_list))
        total_joltage += joltage

    return total_joltage


if __name__ == "__main__":
    with open("testing/inputs/day3.txt", "r") as f:
        input = f.read()

    res_1 = part_1(input)
    print(f"Part 1 answer = {res_1}")

    res_2 = part_2(input)
    print(f"Part 2 answer = {res_2}")
