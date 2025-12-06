# %%
import pandas as pd

# %%
with open("input.txt", "r") as f:
    input_string = f.read()


# %%
def brute_force_count_fresh_ids(input_string):
    input_list = input_string.split("\n\n")
    fresh_range = input_list[0]

    fresh_range_list = fresh_range.split("\n")

    fresh_ids = []
    for fresh_range in fresh_range_list:
        range_list = fresh_range.split("-")
        lower = int(range_list[0])
        upper = int(range_list[1])

        fresh_ids.extend([i for i in range(lower, upper + 1)])

    return len(set(fresh_ids))


# %%
def count_fresh_ids(input_string):
    input_list = input_string.split("\n\n")
    fresh_ranges = input_list[0]
    fresh_ranges_list = fresh_ranges.split("\n")

    lowers = [int(fresh_range.split("-")[0]) for fresh_range in fresh_ranges_list]
    uppers = [int(fresh_range.split("-")[1]) for fresh_range in fresh_ranges_list]

    range_df = (
        pd.DataFrame({"lower": lowers, "upper": uppers})
        .sort_values("lower")
        .reset_index()
    )

    final_lowers = [range_df["lower"][0]]
    final_uppers = [range_df["upper"][0]]
    for _, row in range_df.iterrows():
        if row["lower"] <= final_uppers[-1] + 1:
            if final_uppers[-1] < row["upper"]:
                final_uppers[-1] = row["upper"]
        else:
            final_lowers.append(row["lower"])
            final_uppers.append(row["upper"])

    fresh_ids_count = 0
    for i in range(len(final_lowers)):
        fresh_ids_count += 1 + final_uppers[i] - final_lowers[i]

    return int(fresh_ids_count)


# %%
