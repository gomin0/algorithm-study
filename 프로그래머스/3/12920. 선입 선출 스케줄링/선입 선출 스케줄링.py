def solution(n, cores):
    if n <= len(cores):
        return n
    
    left, right = 0, max(cores) * n
    while left < right:
        mid = (left + right) // 2
        finish = sum(1 + (mid // c) for c in cores)
        if finish >= n:
            right = mid
        else:
            left = mid + 1
    time = left
    
    finish_before_time = sum(1 + (time - 1) // c for c in cores)
    
    for i, c in enumerate(cores):
        if time % c == 0:
            finish_before_time +=1
            if finish_before_time == n:
                return i+1