# %%
with open("input.txt", "r") as f:
    input_string = f.read()


# %%
def count_timelines(input_string):
    input_list = input_string.split("\n")
    input_list.pop()

    for i in range(len(input_list)):
        input_list[i] = input_list[i].replace("|", "0")
        input_list[i] = input_list[i].replace(".", "0")
        input_list[i] = input_list[i].replace("S", "1")
        input_list[i] = input_list[i].replace("^", "9")

    for i in range(len(input_list)):
        input_list[i] = list(map(int, list(input_list[i])))
        input_list[i] = list(map(lambda x: -1 if x == 9 else x, input_list[i]))

    for i in range(1, len(input_list)):
        if -1 in input_list[i]:
            index_list_split = [
                index for index, value in enumerate(input_list[i]) if value == -1
            ]
            index_list_above_non_0 = [
                index for index, value in enumerate(input_list[i - 1]) if value != 0
            ]

            for index in index_list_above_non_0:
                if input_list[i][index] != -1:
                    input_list[i][index] = input_list[i - 1][index]

            for index in index_list_split:
                input_list[i + 1][index - 1] += input_list[i - 1][index]
                input_list[i + 1][index + 1] += input_list[i - 1][index]

        else:
            index_list_above_non_split_non_0 = [
                index for index, value in enumerate(input_list[i - 1]) if value > 0
            ]

            for index in index_list_above_non_split_non_0:
                input_list[i][index] += input_list[i - 1][index]

    timeline_count = sum(input_list[-1])
    return timeline_count
