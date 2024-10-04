from collections import deque

def solution(n, computers):
    def bfs(start):
        queue = deque([start])
        visited[start] = True
        
        while queue:
            node = queue.popleft()
            
            for i in range(n):
                if computers[node][i] == 1 and not visited[i]:
                    queue.append(i)
                    visited[i] = True
                    
    visited = [False for _ in range(n)]
    
    count = 0
    for i in range(n):
        if not visited[i]:
            bfs(i)
            count += 1
            
    return count