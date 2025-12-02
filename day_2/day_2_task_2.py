# %%
with open("input.txt", "r") as f:
    input_string = f.read()

input_list = input_string.split(",")
input_list[-1] = input_list[-1].replace("\n", "")


# %%
def sum_more_invalid_ids(input_list):
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

                    # print(num_parts)
                    if len(set(num_parts)) == 1:
                        # print(num_parts)
                        # print(set(num_parts))
                        # print(i)
                        invalid_sum += i
                        break
    return invalid_sum


# %%
