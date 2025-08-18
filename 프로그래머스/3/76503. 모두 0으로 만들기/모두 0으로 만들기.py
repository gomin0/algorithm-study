from collections import defaultdict, deque

def solution(a, edges):
    if sum(a) != 0:
        return -1
    
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    n = len(a)
    parent = [-1] * n
    order = []
    stack = [0]
    parent[0] = 0
    while stack:
        u = stack.pop()
        order.append(u)
        for v in graph[u]:
            if parent[v] == -1:
                parent[v] = u
                stack.append(v)
                
    answer = 0
    for u in reversed(order):
        p = parent[u]
        if u == 0:
            continue
        answer += abs(a[u])
        a[p] += a[u]
        a[u] = 0
    
    return answer