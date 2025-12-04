# %%
with open("input.txt", "r") as f:
    input_string = f.read()

input_list = input_string.split("\n")
input_list.pop()


# %%
def get_maximum_joltage(input_list):
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


# %%
