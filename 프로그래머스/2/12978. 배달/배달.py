def floyd(N, graph):
    for k in range(1, N+1):
        for i in range(1, N+1):
            for j in range(1, N+1):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
    return graph


def solution(N, road, K):
    answer = 0
    graph = [[float('inf')] * (N+1) for _ in range(N+1)]
    for i in range(1, N+1):
        graph[i][i] = 0
    for a, b, c in road:
        graph[a][b] = min(graph[a][b], c)
        graph[b][a] = min(graph[b][a], c)
    graph = floyd(N, graph)
    
    answer = 0
    for i in range(1, N+1):
        if graph[1][i] <= K:
            answer += 1

    return answer