import sys
sys.setrecursionlimit(10**6)  # 파이썬의 기본 재귀 깊이 제한을 늘림

def solution(nodeinfo):
    nodes = [{'x': x, 'y': y, 'idx': i + 1} for i, (x, y) in enumerate(nodeinfo)]
    nodes.sort(key=lambda n: (-n['y'], n['x']))  # y 내림차순, x 오름차순으로 정렬
    
    def make_tree(nodes):
        if not nodes:
            return None
        
        root = nodes[0]  # 가장 위(y가 가장 크고, x가 작은 노드)가 루트
        left_nodes = [node for node in nodes[1:] if node['x'] < root['x']]
        right_nodes = [node for node in nodes[1:] if node['x'] > root['x']]
        
        root['left'] = make_tree(left_nodes)  # 왼쪽 서브트리 생성
        root['right'] = make_tree(right_nodes)  # 오른쪽 서브트리 생성
        
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
    
    root = make_tree(nodes)  # 트리 생성
    
    return [preorder(root, []), postorder(root, [])]