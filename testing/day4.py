from scipy.signal import convolve2d
import numpy as np


def part_1(input):
    replacements = str.maketrans({"@": "1 ", ".": "0 ", "\n": ";"})
    input_matrix = np.matrix(input.translate(replacements)[:-1])

    neighbour_matrix = convolve2d(
        input_matrix, [[1, 1, 1], [1, 0, 1], [1, 1, 1]], mode="same"
    )

    roll_neighbour_matrix = np.where(input_matrix == 0, 9, neighbour_matrix)
    roll_neighbour_matrix_1 = np.where(
        roll_neighbour_matrix < 4, 1, roll_neighbour_matrix
    )
    accessible_matrix = np.where(
        roll_neighbour_matrix_1 >= 4, 0, roll_neighbour_matrix_1
    )

    return int(accessible_matrix.sum())


def part_2(input):
    replacements = str.maketrans({"@": "1 ", ".": "0 ", "\n": ";"})
    input_matrix = np.matrix(input.translate(replacements)[:-1])

    total_rolls_removed = 0
    rolls_removed = 1
    count = 0
    while rolls_removed > 0:
        neighbour_matrix = convolve2d(
            input_matrix, [[1, 1, 1], [1, 0, 1], [1, 1, 1]], mode="same"
        )

        roll_neighbour_matrix = np.where(input_matrix == 0, 9, neighbour_matrix)
        roll_neighbour_matrix_1 = np.where(
            roll_neighbour_matrix < 4, 1, roll_neighbour_matrix
        )
        accessible_matrix = np.where(
            roll_neighbour_matrix_1 >= 4, 0, roll_neighbour_matrix_1
        )

        input_matrix = np.where(accessible_matrix == 1, 0, input_matrix)

        rolls_removed = int(accessible_matrix.sum())
        total_rolls_removed += rolls_removed

        count += 1

    return total_rolls_removed


if __name__ == "__main__":
    with open("testing/inputs/day4.txt", "r") as f:
        input = f.read()

    res_1 = part_1(input)
    print(f"Part 1 answer = {res_1}")

    res_2 = part_2(input)
    print(f"Part 2 answer = {res_2}")
