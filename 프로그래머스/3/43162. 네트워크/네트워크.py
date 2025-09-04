from collections import deque, defaultdict

def solution(n, computers):
    visited = set()
    network = defaultdict(list)
    for i in range(n):
        for j in range(n):
            if i != j and computers[i][j] == 1:
                network[i].append(j)
                network[j].append(i)
    def bfs(n):
        q = deque()
        q.append(n)
        visited.add(n)
        while q:
            node = q.popleft()
            for next_node in network[node]:
                if next_node not in visited:
                    q.append(next_node)
                    visited.add(next_node)
    
    answer = 0
    for i in range(n):
        if i not in visited:
            answer += 1
            bfs(i)
    
    return answer