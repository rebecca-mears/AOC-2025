# %%
with open("input.txt", "r") as f:
    input_string = f.read()

input_string = input_string.replace("L", "-").replace("R", "")
input = input_string.split("\n")
input.pop()

input_list = list(map(int, input))


# %%
def count_0s(input_list: list) -> int:
    count = 0
    dial = 50

    for input in input_list:
        dial += input

        if dial % 100 == 0:
            count += 1

    return count


# %%
print(count_0s(input_list))
