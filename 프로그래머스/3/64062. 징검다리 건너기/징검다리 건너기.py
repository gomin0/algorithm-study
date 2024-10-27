# 이분 탐색으로 건널 수 있는 사람 수 찾기

def solution(stones, k):

    def possible(mid):
        count = 0  # 못 건너는 연속 돌
        
        for stone in stones:
            if stone < mid:
                count += 1
                if count >= k:
                    return False
            else:
                count = 0
        return True
    
    left, right = 0, max(stones)
    
    while left <= right:
        mid = (left + right) // 2
        if possible(mid):
            left = mid + 1
        else:
            right = mid - 1
            
    return right