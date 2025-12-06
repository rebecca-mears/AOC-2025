# %%
import pandas as pd

# %%
with open("input.txt", "r") as f:
    input_string = f.read()


# %%
def maths_homework(input_string):
    input_rows = input_string.split("\n")
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
