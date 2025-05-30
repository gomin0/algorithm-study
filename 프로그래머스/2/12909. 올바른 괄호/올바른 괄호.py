def solution(s):
    count: int = 0
    
    for p in s:
        if p == '(':
            count += 1
        if p == ')':
            count -= 1
        if count < 0:
            return False
    
    if count != 0:
        return False
    return True