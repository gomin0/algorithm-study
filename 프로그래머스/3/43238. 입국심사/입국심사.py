def solution(n, times):
    min_time: int = 1
    max_time: int = max(times) * n
    
    while min_time <= max_time:
        mid: int = (min_time + max_time) // 2
        count: int = 0
        for time in times:
            count += mid // time
        if count >= n:
            max_time = mid - 1
        else:
            min_time = mid + 1
    
    return min_time