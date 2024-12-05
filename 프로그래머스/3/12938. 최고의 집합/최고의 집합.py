def solution(n, s):
    
    if s < n:
        return [-1]
    
    a = s // n
    b = s % n
    
    answer = [a for _ in range(n)]
    for i in range(n - 1, -1, -1):
        if b > 0:
            answer[i] += 1
            b -= 1
        else:
            break
        
    return answer