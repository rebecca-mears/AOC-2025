# %%
from math import ceil, floor

# %%
with open("input.txt", "r") as f:
    input_string = f.read()

input_string = input_string.replace("L", "-").replace("R", "")
input = input_string.split("\n")
input.pop()

input_list = list(map(int, input))


# %%
def count_all_0s(input_list: list) -> int:
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


# %%
print(count_all_0s(input_list))

# %%
