#크루스칼 알고리즘
def find(parent, x):  # 루트 노드 찾기
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, rank, x, y):
    rootx = find(parent, x)
    rooty = find(parent, y)
    
    if rootx != rooty:
        if rank[rootx] > rank[rooty]:
            parent[rooty] = rootx
        elif rank[rootx] < rank[rooty]:
            parent[rootx] = rooty
        else:
            parent[rooty] = rootx
            rank[rootx] += 1
            
def kruskal(n, edges):
    parent = [i for i in range(n)]
    rank = [0] * n
    
    edges.sort(key=lambda x: x[2])
    
    mst = []
    total_weight = 0
    
    for edge in edges:
        u, v, weight = edge
        if find(parent, u) != find(parent,v):
            union(parent, rank, u, v)
            mst.append(edge)
            total_weight += weight
    return mst, total_weight

def solution(n, costs):
    mst, total_weight = kruskal(n, costs)
    return total_weight