def solution(a):
    answer = 2  # 왼쪽 끝 + 오른쪽 끝
    
    n = len(a)
    
    left_min = [0] * n
    right_min = [0] * n
    
    left_min[0] = a[0]
    for i in range(1, n):
        left_min[i] = min(left_min[i-1], a[i])
    
    right_min[n-1] = a[n-1]
    for i in range(n-2, -1, -1):
        right_min[i] = min(right_min[i+1], a[i])
    
    for i in range(1, len(a) - 1):
        
        if not (a[i] > left_min[i] and a[i] > right_min[i]):
            answer += 1
            
    return answer