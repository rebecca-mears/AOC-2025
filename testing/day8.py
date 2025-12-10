from scipy.spatial.distance import pdist, squareform
import pandas as pd
import numpy as np


def part_1(input):
    input_list = input.split("\n")
    input_list.pop()

    input_vectors = list(map(lambda x: list(map(int, x.split(","))), input_list))

    distance_matrix = squareform(pdist(input_vectors, metric="euclidean"))
    distance_matrix_df = pd.DataFrame(distance_matrix).replace(0, np.nan)

    connections = []
    for _ in range(1000):
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

    sorted_connections = sorted(connections, key=lambda item: len(item))

    product = (
        len(sorted_connections[-1])
        * len(sorted_connections[-2])
        * len(sorted_connections[-3])
    )

    return product


def part_2(input):
    input_list = input.split("\n")
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

    product = input_vectors[closest_boxes[0]][0] * input_vectors[closest_boxes[1]][0]

    return product


if __name__ == "__main__":
    with open("testing/inputs/day8.txt", "r") as f:
        input = f.read()

    res_1 = part_1(input)
    print(f"Part 1 answer = {res_1}")

    res_2 = part_2(input)
    print(f"Part 2 answer = {res_2}")
