def solution(n, costs):
    costs.sort(key=lambda x:x[2])
    parent: list[int] = [i for i in range(n)]
    
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(a, b):
        a_parent: int = find(a)
        b_parent: int = find(b)
        if a_parent != b_parent:
            parent[b_parent] = a_parent
            return True
        return False
    
    answer: int = 0
    for a, b, c in costs:
        if union(a, b):
            answer += c
    
    return answer