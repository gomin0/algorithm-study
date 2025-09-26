from collections import defaultdict
import heapq


def solution(n, computers):
    visited = set()
    graph = defaultdict(list)
    for i in range(n):
        for j in range(n):
            if i != j and computers[i][j] == 1:
                graph[i].append(j)
                graph[j].append(i)
    
    def dfs(start, graph):
        stack = []
        stack.append(start)
        visited.add(start)
        while stack:
            node = stack.pop()
            for next_node in graph[node]:
                if next_node not in visited:
                    visited.add(next_node)
                    stack.append(next_node)
            
        
    # def bfs(node, graph):
    answer = 0
    for i in range(n):
        if i not in visited:
            dfs(i, graph)
            answer += 1
    
    return answer