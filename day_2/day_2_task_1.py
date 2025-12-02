# %%
with open("input.txt", "r") as f:
    input_string = f.read()

input_list = input_string.split(",")
input_list[-1] = input_list[-1].replace("\n", "")


# %%
def sum_invalid_ids(input_list):
    invalid_sum = 0

    for input_range in input_list:
        input_range_list = input_range.split("-")
        first = input_range_list[0]
        last = input_range_list[1]

        for i in range(int(first), int(last) + 1):
            if len(str(i)) % 2 == 0:
                # print(i)
                first_half = str(i)[: int(len(str(i)) / 2)]
                second_half = str(i)[int(len(str(i)) / 2) :]

                if first_half == second_half:
                    # print(i)
                    invalid_sum += i

    return invalid_sum
