# %%
with open("input.txt", "r") as f:
    input_string = f.read()

input_list = input_string.split("\n")
input_list.pop()

# %%


def get_highest_joltage(input_list):
    total_joltage = 0

    for bank in input_list:
        first_digit = max(bank[:-1])
        bank_remaining = bank.split(first_digit, 1)[1]

        second_digit = max(bank_remaining)

        joltage = int(first_digit + second_digit)
        total_joltage += joltage

    return total_joltage
