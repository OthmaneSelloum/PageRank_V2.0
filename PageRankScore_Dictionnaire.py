import PageRankScore as PR


def page_rank_score(Dict, epsilon=1e-6):
    N = len(Dict)

    mat_adj = [[0] * N for _ in range(N)]

    for node, neighbors in Dict.items():
        for neighbor in neighbors:
            mat_adj[node][neighbor] = 1

    return PR.page_rank_score(mat_adj, epsilon)
