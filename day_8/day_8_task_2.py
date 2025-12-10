# %%
from scipy.spatial.distance import pdist, squareform
import pandas as pd
import numpy as np

# %%
with open("input.txt", "r") as f:
    input_string = f.read()


# %%
def get_product_last_x(input_string):
    input_list = input_string.split("\n")
    input_list.pop()

    input_vectors = list(map(lambda x: list(map(int, x.split(","))), input_list))

    distance_matrix = squareform(pdist(input_vectors, metric="euclidean"))
    distance_matrix_df = pd.DataFrame(distance_matrix).replace(0, np.nan)

    connections = [[distance_matrix_df.stack().idxmin()[0]]]
    while len(sorted(connections, key=lambda item: len(item))[-1]) < 1000:
        closest_boxes = distance_matrix_df.stack().idxmin()

        if not any(closest_boxes[0] in connection for connection in connections):
            connections.append([closest_boxes[0]])

        list_idx_0 = [
            index
            for index, connection in enumerate(connections)
            if closest_boxes[0] in connection
        ]

        if any(closest_boxes[1] in connection for connection in connections):
            list_idx_1 = [
                index
                for index, connection in enumerate(connections)
                if closest_boxes[1] in connection
            ]
            if list_idx_0[0] != list_idx_1[0]:
                connections[list_idx_0[0]].extend(connections[list_idx_1[0]])
                connections.pop(list_idx_1[0])
        else:
            connections[list_idx_0[0]].append(closest_boxes[1])

        distance_matrix_df[closest_boxes[0]][closest_boxes[1]] = np.nan
        distance_matrix_df[closest_boxes[1]][closest_boxes[0]] = np.nan

        print(len(sorted(connections, key=lambda item: len(item))[-1]))

    product = input_vectors[closest_boxes[0]][0] * input_vectors[closest_boxes[1]][0]

    return product
