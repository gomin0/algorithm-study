def is_possible_tree(tree_str):
    if len(tree_str) == 1:
        return True
    
    mid: int = len(tree_str) // 2
    root: str = tree_str[mid]
    left_sub: str = tree_str[:mid]
    right_sub: str = tree_str[mid+1:]
    
    if root == '0' and ('1' in left_sub or '1' in right_sub):
        return False
    return is_possible_tree(left_sub) and is_possible_tree(right_sub)

def solution(numbers):
    answer = []
    for number in numbers:
        bin_str: str = f"{number:b}"
        length: int = len(bin_str)
        size: int = 1
        while size < length:
            size = size * 2 + 1
        bin_str = bin_str.zfill(size)
        answer.append(1) if is_possible_tree(bin_str) else answer.append(0)
        
    return answer