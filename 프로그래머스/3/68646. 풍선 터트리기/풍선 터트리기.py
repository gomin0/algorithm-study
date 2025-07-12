def solution(a) -> int:
    answer: int = 0
    length: int = len(a)
    min_left: list[int] = [0] * length
    min_right: list[int] = [0] * length
    
    min_left[0] = a[0]
    for i in range(1, length):
        min_left[i] = min(min_left[i-1], a[i])
    min_right[-1] = a[-1]
    for i in range(length-2, -1, -1):
        min_right[i] = min(min_right[i+1], a[i])
    
    for i in range(length):
        if i == 0 or i == length-1:
            answer += 1
            continue
        if min_left[i-1] < a[i] and min_right[i+1] < a[i]:
            continue
        answer += 1
    
    return answer