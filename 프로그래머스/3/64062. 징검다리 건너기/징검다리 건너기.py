def solution(stones, k):
    answer: int = 0
    left: int = 0
    right: int = max(stones)
    
    while left <= right:
        mid: int = (left + right) // 2
        count: int = 0
        possible: bool = True
        for stone in stones:
            if stone < mid:
                count += 1
                if count >= k:
                    possible = False
                    break
            else:
                count = 0
                
        if possible:
            answer = mid
            left = mid + 1
        else:
            right = mid - 1
    
    return answer