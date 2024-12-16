def solution(stones, k):
    left = 0
    right = max(stones)
    
    while left <= right:
        mid = (left + right) // 2
        possible = True
        
        count = 0
        for stone in stones:
            if stone < mid:
                count += 1
                if count >= k:
                    possible = False
                    break
            else:
                count = 0    
        
        if possible:
            left = mid + 1
        else:
            right = mid - 1
        
    return right