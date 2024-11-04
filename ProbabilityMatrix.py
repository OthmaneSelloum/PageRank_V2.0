import numpy as np


def matrice_probability(adj_mat, damping=0.85):
    adj_mat = np.array(adj_mat)
    N = adj_mat.shape[0]
    mat_prob = np.zeros((N, N))

    for i in range(N):
        outgoing_links_sum = np.sum(adj_mat[i, :])
        if outgoing_links_sum != 0:
            for j in range(N):
                mat_prob[i, j] = (damping * adj_mat[i, j] / outgoing_links_sum) + (1 - damping) / N
        else:
            mat_prob[i, :] = 1 / N

    return mat_prob
