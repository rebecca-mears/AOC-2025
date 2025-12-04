# %%
from scipy.signal import convolve2d
import numpy as np

# %%
with open("input.txt", "r") as f:
    input_string = f.read()


# %%
def get_number_accessable_rolls(input_string):
    replacements = str.maketrans({"@": "1 ", ".": "0 ", "\n": ";"})
    input_matrix = np.matrix(input_string.translate(replacements)[:-1])

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


# %%
