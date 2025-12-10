def rectangle_area(a, b):
    x = abs(a[0] - b[0] + 1)
    y = abs(a[1] - b[1] + 1)
    return x * y


def part_1(input):
    input_list = input.split("\n")
    input_list.pop()

    input_vectors = list(map(lambda x: list(map(int, x.split(","))), input_list))

    rectangle_area_matrix = [
        [rectangle_area(a, b) for a in input_vectors] for b in input_vectors
    ]

    return max(max(row) for row in rectangle_area_matrix)


def part_2(input):
    1 + 1


if __name__ == "__main__":
    with open("testing/inputs/day9.txt", "r") as f:
        input = f.read()

    res_1 = part_1(input)
    print(f"Part 1 answer = {res_1}")

    res_2 = part_2(input)
    print(f"Part 2 answer = {res_2}")
