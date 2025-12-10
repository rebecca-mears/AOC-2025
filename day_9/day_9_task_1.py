# %%
with open("input.txt", "r") as f:
    input_string = f.read()


# %%
def rectangle_area(a, b):
    x = abs(a[0] - b[0] + 1)
    y = abs(a[1] - b[1] + 1)
    return x * y


# %%
def find_largest_area(input_string):
    input_list = input_string.split("\n")
    input_list.pop()

    input_vectors = list(map(lambda x: list(map(int, x.split(","))), input_list))

    rectangle_area_matrix = [
        [rectangle_area(a, b) for a in input_vectors] for b in input_vectors
    ]

    return max(max(row) for row in rectangle_area_matrix)
