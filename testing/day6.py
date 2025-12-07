import pandas as pd


def part_1(input):
    input_rows = input.split("\n")
    input_rows.pop()

    number_1 = input_rows[0].split()
    number_2 = input_rows[1].split()
    number_3 = input_rows[2].split()
    number_4 = input_rows[3].split()
    operation = input_rows[4].split()

    homework_df = pd.DataFrame(
        {
            "number_1": number_1,
            "number_2": number_2,
            "number_3": number_3,
            "number_4": number_4,
            "operation": operation,
        }
    ).astype(
        {
            "number_1": int,
            "number_2": int,
            "number_3": int,
            "number_4": int,
        }
    )

    homework_df["answer_+"] = (
        homework_df[["number_1", "number_2", "number_3", "number_4"]].sum(axis=1)
    ).where(homework_df["operation"] == "+")

    homework_df["answer_*"] = (
        homework_df["number_1"]
        * homework_df["number_2"]
        * homework_df["number_3"]
        * homework_df["number_4"]
    ).where(homework_df["operation"] == "*")

    answer_add_sum = homework_df["answer_+"].sum()
    answer_multiply_sum = homework_df["answer_*"].sum()

    return int(answer_add_sum + answer_multiply_sum)


def part_2(input):
    input_rows = input.split("\n")
    input_rows.pop()

    for i in range(len(input_rows[0])):
        if (
            (input_rows[0][i] == " ")
            & (input_rows[1][i] == " ")
            & (input_rows[2][i] == " ")
            & (input_rows[3][i] == " ")
        ):
            input_rows[0] = input_rows[0][:i] + "|" + input_rows[0][i + 1 :]
            input_rows[1] = input_rows[1][:i] + "|" + input_rows[1][i + 1 :]
            input_rows[2] = input_rows[2][:i] + "|" + input_rows[2][i + 1 :]
            input_rows[3] = input_rows[3][:i] + "|" + input_rows[3][i + 1 :]

    number_1 = input_rows[0].split("|")
    number_2 = input_rows[1].split("|")
    number_3 = input_rows[2].split("|")
    number_4 = input_rows[3].split("|")
    operation = input_rows[4].split()

    homework_df = pd.DataFrame(
        {
            "number_1": number_1,
            "number_2": number_2,
            "number_3": number_3,
            "number_4": number_4,
            "operation": operation,
        }
    )

    for i in range(1, 5):
        homework_df[f"new_{i}"] = (
            homework_df["number_1"].str[4 - i]
            + homework_df["number_2"].str[4 - i]
            + homework_df["number_3"].str[4 - i]
            + homework_df["number_4"].str[4 - i]
        ).astype(float)

    homework_df.loc[homework_df["operation"] == "+"] = homework_df.fillna(0)
    homework_df.loc[homework_df["operation"] == "*"] = homework_df.fillna(1)

    homework_df["answer_+"] = (
        homework_df[["new_1", "new_2", "new_3", "new_4"]].sum(axis=1)
    ).where(homework_df["operation"] == "+")

    homework_df["answer_*"] = (
        homework_df["new_1"]
        * homework_df["new_2"]
        * homework_df["new_3"]
        * homework_df["new_4"]
    ).where(homework_df["operation"] == "*")

    answer_add_sum = homework_df["answer_+"].sum()
    answer_multiply_sum = homework_df["answer_*"].sum()

    return answer_add_sum + answer_multiply_sum


if __name__ == "__main__":
    with open("testing/inputs/day6.txt", "r") as f:
        input = f.read()

    res_1 = part_1(input)
    print(f"Part 1 answer = {res_1}")

    res_2 = part_2(input)
    print(f"Part 2 answer = {res_2}")
