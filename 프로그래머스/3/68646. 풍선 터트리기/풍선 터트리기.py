def solution(a):
    n = len(a)
    left_min = [0] * n
    right_min = [0] * n
    left_min[0] = a[0]
    right_min[n-1] = a[n-1]
    for i in range(1, n):
        left_min[i] = min(left_min[i-1], a[i])
    for i in range(n-2, -1, -1):
        right_min[i] = min(right_min[i+1], a[i])
    
    answer = 0
    for i in range(n):
        if i == 0 or i == n-1:
            answer += 1
            continue
        if left_min[i-1] < a[i] and right_min[i+1] < a[i]:
            continue
        answer += 1
            
    return answer