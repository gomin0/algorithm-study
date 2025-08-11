def solution(distance, rocks, n):
    answer = 0
    rocks.sort()
    rocks.append(distance)
    
    left, right = 1, distance
    while left <= right:
        mid = (left + right) // 2
        current = 0
        remove = 0
        for rock in rocks:
            if rock - current < mid:
                remove += 1
            else:
                current = rock
        if remove <= n:
            answer = mid
            left = mid + 1
        else:
            right = mid - 1
            
    return answer