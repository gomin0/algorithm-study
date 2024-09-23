import bisect

def solution(diffs, times, limit):
    answer = 0
    length = len(diffs)
    
    def solve(level):
        total_time = 0  # 총 시간
        for i in range(length):
            if diffs[i] <= level:
                total_time += times[i]
            else:
                error = diffs[i] - level
                total_time += times[i] * (error+1) + times[i-1] * error
        if total_time > limit:
            return False
        return True

    low, high = 1, max(diffs)
    while low <= high:
        mid = (low + high) // 2
        if solve(mid):
            answer = mid
            high = mid - 1
        else:
            low = mid + 1
    return answer