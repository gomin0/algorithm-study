def solution(n, s):
    
    if n > s:
        return [-1]
    if n == s:
        return [1] * n
    
    a = s // n
    b = s % n
    
    answer = [a] * n
    
    for i in range(b):
        answer[i] += 1
    
    return sorted(answer)