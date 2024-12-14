def find(parent, node):
    if node != parent[node]:
        parent[node] = find(parent, parent[node])
    return parent[node]

def union(px, py, parent, rank):
    if rank[px] > rank[py]:
        parent[py] = px
    elif rank[py] > rank[px]:
        parent[px] = py
    else:
        parent[py] = px
        rank[px] += 1

def solution(n, costs):
    answer = 0
    
    parent = [i for i in range(n)]
    rank = [0 for _ in range(n)]
    
    costs.sort(key=lambda x:x[2])
    
    for x, y, cost in costs:
        px = find(parent, x)
        py = find(parent, y)
        if px != py:
            union(px, py, parent, rank)
            answer += cost
    
    return answer