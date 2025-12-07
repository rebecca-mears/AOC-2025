import pandas as pd


def part_1(input_string):
    input_list = input_string.split("\n\n")
    fresh_range = input_list[0]
    ingredients = input_list[1]

    fresh_range_list = fresh_range.split("\n")

    ingredients_list = ingredients.split("\n")
    ingredients_list.pop()

    fresh_ingredients = []
    for ingredient in ingredients_list:
        ingredient = int(ingredient)
        for range in fresh_range_list:
            range_list = range.split("-")
            lower = int(range_list[0])
            upper = int(range_list[1])

            if (ingredient >= lower) & (ingredient <= upper):
                fresh_ingredients.append(ingredient)
                break

    return len(set(fresh_ingredients))


def part_2(input_string):
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


if __name__ == "__main__":
    with open("testing/inputs/day5.txt", "r") as f:
        input = f.read()

    res_1 = part_1(input)
    print(f"Part 1 answer = {res_1}")

    res_2 = part_2(input)
    print(f"Part 2 answer = {res_2}")
