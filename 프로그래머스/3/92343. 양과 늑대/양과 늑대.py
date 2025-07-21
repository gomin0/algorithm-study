from collections import defaultdict

def solution(info, edges):
    answer: int = 0
    tree: defaultdict[int, list[int]] = defaultdict(list)
    for parent, child in edges:
        tree[parent].append(child)
        
    def dfs(node, sheep, wolf, next_nodes):
        if info[node] == 0:
            sheep += 1
        else:
            wolf += 1
        if wolf >= sheep:
            return sheep
        max_sheep = sheep
        
        for i, next_node in enumerate(next_nodes):
            max_sheep = max(
                max_sheep,
                dfs(
                    next_node,
                    sheep,
                    wolf,
                    next_nodes[:i] + next_nodes[i+1:] + tree[next_node]
                )
            )
        
        return max_sheep
    
    return dfs(0, 0, 0, tree[0])