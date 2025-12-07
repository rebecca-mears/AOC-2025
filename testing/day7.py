def part_1(input):
    input_list = input.split("\n")
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


def part_2(input):
    input_list = input.split("\n")
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


if __name__ == "__main__":
    with open("testing/inputs/day7.txt", "r") as f:
        input = f.read()

    res_1 = part_1(input)
    print(f"Part 1 answer = {res_1}")

    res_2 = part_2(input)
    print(f"Part 2 answer = {res_2}")
