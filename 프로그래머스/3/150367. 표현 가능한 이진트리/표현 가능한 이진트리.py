def check(binary):
    mid = len(binary) // 2  # 루트 노드 위치
    root = binary[mid]
    
    if root == '0' and '1' in binary:
        return False
    
    if len(binary) > 1:
        return check(binary[:mid]) and check(binary[mid+1:])  # 서브 트리에 대해 재귀
    
    return True

def solution(numbers):
    answer = []
    
    for number in numbers:
        binary = bin(number)[2:]  # 앞에 0b 떼기
        
        length = len(binary)
        tree_size = 1
        while tree_size -1 < length:
            tree_size *= 2
        tree_size -= 1  # 2^n - 1
        
        full_binary = binary.zfill(tree_size)
        
        answer.append(1 if check(full_binary) else 0)
    
    return answer