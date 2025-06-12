def solution(n, s):
    div: int = s // n
    if div == 0:
        return [-1]
    rest: int = s % n
    answer: list[int] = [div] * n
    for i in range(rest):
        answer[n - i - 1] += 1
    
    return answer