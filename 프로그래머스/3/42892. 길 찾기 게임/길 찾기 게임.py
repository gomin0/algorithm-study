import sys
sys.setrecursionlimit(10**6)  # 파이썬의 기본 재귀 깊이 제한을 늘림
def solution(nodeinfo):
    answer = [[]]
    
    nodes = [{'x': x, 'y': y, 'idx': i+1} for i, (x, y) in enumerate(nodeinfo)]
    
    nodes.sort(key=lambda n: (-n['y'], n['x']))  # 트리 만들기
    
    def make_tree(nodes):
        if not nodes:
            return None
        
        root = nodes[0]
        left_nodes = [node for node in nodes[1:] if node['x'] < root['x']]
        right_nodes = [node for node in nodes[1:] if node['x'] > root['x']]
        
        root['left'] = make_tree(left_nodes)
        root['right'] = make_tree(right_nodes)
        
        return root
    
    def preorder(node, traversal):
        if node:
            traversal.append(node['idx'])  # 현재 노드 방문
            preorder(node['left'], traversal)  # 왼쪽 서브트리 탐색
            preorder(node['right'], traversal)  # 오른쪽 서브트리 탐색
        return traversal
    
    def postorder(node, traversal):
        if node:
            postorder(node['left'], traversal)  # 왼쪽 서브트리 탐색
            postorder(node['right'], traversal)  # 오른쪽 서브트리 탐색
            traversal.append(node['idx'])  # 현재 노드 방문
        return traversal
    
    root = make_tree(nodes)
    
    return [preorder(root, []), postorder(root, [])]