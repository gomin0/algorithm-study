def solution(n, stations, w):
    answer: int = 0
    coverage: int = 2 * w + 1
    idx: int = 1
    i: int = 0
    length: int = len(stations)
    
    while idx <= n:
        if i < length and stations[i] - w <= idx <= stations[i] + w:
            idx = stations[i] + w + 1
            i += 1
        else:
            answer += 1
            idx += coverage
    
    return answer
