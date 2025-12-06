# %%
with open("input.txt", "r") as f:
    input_string = f.read()


# %%
def count_fresh_ingredients(input_string):
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


# %%
