def solution(n, wires):
    answer = n
    
    graph = [[0] * (n+1) for _ in range(n+1)]
    
    def bfs(start):
        visited = [False] * (n+1)
        count = 1
        stack = []
        visited[start] = True
        stack.append(start)
        
        while stack:
            temp = stack.pop(0)
            
            for q in range(1, n + 1):
                if graph[temp][q] == 1 and not visited[q]:
                    visited[q] = True
                    stack.append(q)
                    count += 1
        return abs(count - (n - count))
    
    for i in wires:
        a, b = i[0], i[1]
        graph[a][b] = 1
        graph[b][a] = 1

    for wire in wires:
        c, d = wire[0], wire[1]
        graph[c][d] = 0 # 하나 빼기
        graph[d][c] = 0
        
        answer = min(answer, bfs(c))
        
        graph[c][d] = 1 # 다시 복구
        graph[d][c] = 1
        
    return answer