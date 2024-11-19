import sys
sys.setrecursionlimit(10**6)

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
    
    def make_tree(nodes, head=None):
        if not nodes:
            return None
        
        node_x, node_y, idx = nodes[0]
        node = Node([node_x, node_y], idx)
        
        if head is None:
            head = node
            
        left_nodes = [n for n in nodes[1:] if n[0] < node_x]
        right_nodes = [n for n in nodes[1:] if n[0] > node_x]
        
        node.left = make_tree(left_nodes, head)
        node.right = make_tree(right_nodes, head)
        
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