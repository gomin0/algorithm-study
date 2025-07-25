def solution(n, results):
    graph: list[list[False]] = [[False] * n for _ in range(n)]
    
    for i in range(n):
        graph[i][i] = True
    for a, b in results:
        graph[a-1][b-1] = True
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if graph[i][k] and graph[k][j]:
                    graph[i][j] = True
    
    answer: int = 0
    for i in range(n):
        count = 0
        for j in range(n):
            if graph[i][j] or graph[j][i]:
                count += 1
        if count == n:
            answer += 1
    
    return answer