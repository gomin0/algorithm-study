def solution(sequence, k):
    length = float('inf')
    n = len(sequence)
    left = 0
    right = 0
    _sum = 0
    answer = []
    while right < n:
        _sum += sequence[right]
        while _sum >= k:
            if _sum == k and length > right - left:
                length = right - left
                answer = [left, right]
            _sum -= sequence[left]
            left += 1
        right += 1
    
    return answer