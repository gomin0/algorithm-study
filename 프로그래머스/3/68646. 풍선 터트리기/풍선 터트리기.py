def solution(a):
    answer = 2
    
    n = len(a)
    
    left_min = [0 for _ in range(n)]
    right_min = [0 for _ in range(n)]
    
    left_min[0] = a[0]
    for i in range(1, n):
        left_min[i] = min(left_min[i-1], a[i])
    
    right_min[n-1] = a[n-1]
    for i in range(n-2, -1, -1):
        right_min[i] = min(right_min[i+1], a[i])
    
    for i in range(1, n-1):
        if not(a[i] > left_min[i] and a[i] > right_min[i]):
            answer += 1
    
    return answer