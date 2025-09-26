from collections import defaultdict, deque
import heapq


def solution(n, computers):
    visited = set()
    graph = defaultdict(list)
    for i in range(n):
        for j in range(n):
            if i != j and computers[i][j] == 1:
                graph[i].append(j)
                graph[j].append(i)
    
    def dfs(start):
        stack = []
        stack.append(start)
        visited.add(start)
        while stack:
            node = stack.pop()
            for next_node in graph[node]:
                if next_node not in visited:
                    visited.add(next_node)
                    stack.append(next_node)
            
    def bfs(start):
        q = deque()
        q.append(start)
        visited.add(start)
        while q:
            node = q.popleft()
            for next_node in graph[node]:
                if next_node not in visited:
                    visited.add(next_node)
                    q.append(next_node)
        
    answer = 0
    for i in range(n):
        if i not in visited:
            # dfs(i)
            bfs(i)
            answer += 1
    
    return answer