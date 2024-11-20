from collections import defaultdict

def solution(info, edges):
    
    tree = defaultdict(list)
    for parent, child in edges:
        tree[parent].append(child)
            
    def dfs(node, sheep, wolf, next_nodes):
        if info[node] == 0:  # 양
            sheep += 1
        else:  # 늑대
            wolf += 1
            
        if sheep <= wolf:
            return sheep
        
        max_sheep = sheep
        
        for n in tree[node]:
            next_nodes.append(n)
        
        for i, next_node in enumerate(next_nodes):
            max_sheep = max(max_sheep, dfs(next_node, sheep, wolf, next_nodes[:i] + next_nodes[i+1:]))
            
        return max_sheep
    
    return dfs(0, 0, 0, [])