import sys
sys.setrecursionlimit(10**6)  # 파이썬의 기본 재귀 깊이 제한은 1000 노드가 최대 10,000개까지 있을 수 있어서 재귀 제한을 늘려주기

class Node:
    def __init__(self, info, idx):
        self.x = info[0]
        self.y = info[1]
        self.idx = idx
        self.left = None
        self.right = None

def solution(nodeinfo):
    nodes = [(x, y, i+1) for i, (x, y) in enumerate(nodeinfo)]
    nodes.sort(key=lambda x: (-x[1], x[0]))
    
    def make_tree(nodes):
        if not nodes:
            return None
        
        node_x, node_y, idx = nodes[0]
        node = Node([node_x, node_y], idx)
            
        left_nodes = [n for n in nodes[1:] if n[0] < node_x]
        right_nodes = [n for n in nodes[1:] if n[0] > node_x]
        
        node.left = make_tree(left_nodes)
        node.right = make_tree(right_nodes)
        
        return node
    
    def preorder(node, traversal):
        if node:
            traversal.append(node.idx)
            preorder(node.left, traversal)
            preorder(node.right, traversal)
        return traversal
    
    def postorder(node, traversal):
        if node:
            postorder(node.left, traversal)
            postorder(node.right, traversal)
            traversal.append(node.idx)
        return traversal
    
    root = make_tree(nodes)
    
    return [preorder(root, []), postorder(root, [])]