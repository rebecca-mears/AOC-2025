# %%
from scipy.spatial.distance import pdist, squareform

# %%
with open("input.txt", "r") as f:
    input_string = f.read()


# %%
def get_product_3_largest(input_string):
    input_list = input_string.split("\n")
    input_list.pop()

    input_vectors = list(map(lambda x: list(map(int, x.split(","))), input_list))

    distance_matrix = squareform(pdist(input_vectors, metric="euclidean"))

    connections = []
    for i in range(len(input_vectors)):
        if not any(i in connection for connection in connections):
            connections.append([i])

        i_list_index = [
            index for index, connection in enumerate(connections) if i in connection
        ]

        closest_box_idx = sorted(
            list(enumerate(distance_matrix[i])), key=lambda item: item[1]
        )[1][0]

        if any(closest_box_idx in connection for connection in connections):
            idx_list_index = [
                index
                for index, connection in enumerate(connections)
                if closest_box_idx in connection
            ]
            if i_list_index[0] != idx_list_index[0]:
                connections[i_list_index[0]].extend(connections[idx_list_index[0]])
                connections.pop(idx_list_index[0])
        else:
            connections[i_list_index[0]].append(closest_box_idx)

    sorted_connections = sorted(connections, key=lambda item: len(item))

    product = (
        len(sorted_connections[-1])
        * len(sorted_connections[-2])
        * len(sorted_connections[-3])
    )

    return product
