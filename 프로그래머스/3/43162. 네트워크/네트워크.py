from collections import deque, defaultdict

def solution(n, computers):
    answer = 0
    
    def bfs(start):
        queue = deque([start])
        visited.add(start)
        
        while queue:
            node = queue.popleft()
            for i in range(n):
                if i != node and computers[node][i] == 1:
                    if not i in visited:
                        visited.add(i)
                        queue.append(i)
            
    visited = set()
    for i in range(n):
        if not i in visited:
            bfs(i)
            answer += 1
    
    return answer