def solution(n, times):
    answer = 0
    
    left = 1
    right = max(times) * n
    
    while left <= right:
        num = 0
        mid = (left + right) // 2
        for time in times:
            num += mid//time
        if num >= n:
            right = mid - 1
        else:
            left = mid + 1
    
    return left