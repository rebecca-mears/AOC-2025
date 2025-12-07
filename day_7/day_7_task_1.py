# %%
with open("input.txt", "r") as f:
    input_string = f.read()


# %%
def count_splits(input_string):
    input_list = input_string.split("\n")
    input_list.pop()

    s_index = input_list[0].index("S")
    input_list[1] = input_list[1][:s_index] + "|" + input_list[1][s_index + 1 :]

    for i in range(2, len(input_list)):
        if "^" in input_list[i]:
            index_list_above = [
                index for index, chr in enumerate(input_list[i - 1]) if chr == "|"
            ]
            index_list = [
                index for index, chr in enumerate(input_list[i]) if chr == "^"
            ]

            for index in index_list:
                if input_list[i - 1][index] != "|":
                    input_list[i] = (
                        input_list[i][:index] + "*" + input_list[i][index + 1 :]
                    )

            for index in index_list_above:
                if input_list[i][index] != "^":
                    input_list[i] = (
                        input_list[i][:index] + "|" + input_list[i][index + 1 :]
                    )

        else:
            index_list_above_split = [
                index for index, chr in enumerate(input_list[i - 1]) if chr == "^"
            ]
            index_list_above_beam = [
                index for index, chr in enumerate(input_list[i - 1]) if chr == "|"
            ]

            for index in index_list_above_split:
                input_list[i] = (
                    input_list[i][: index - 1]
                    + "|"
                    + input_list[i][index]
                    + "|"
                    + input_list[i][index + 2 :]
                )

            for index in index_list_above_beam:
                input_list[i] = input_list[i][:index] + "|" + input_list[i][index + 1 :]

    split_count = 0
    for row in input_list:
        split_count += row.count("^")

    return split_count
