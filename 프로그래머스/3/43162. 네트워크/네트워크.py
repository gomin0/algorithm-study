from collections import deque

def solution(n, computers):
    answer: int = 0
    
    def bfs(start):
        visited.add(start)
        queue: deque = deque([start])
        
        while queue:
            node = queue.popleft()
            for i in range(n):
                if i != node and computers[node][i] == 1 and i not in visited:
                    visited.add(i)
                    queue.append(i)
    
    visited: set[int] = set()
    for i in range(n):
        if i not in visited:
            bfs(i)
            answer += 1
    
    return answer