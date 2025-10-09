def solution(n, stations, w):
    answer = 0
    cover = 2 * w + 1
    length = len(stations)
    i = 1
    idx = 0
    while i <= n:
        if idx < length and stations[idx] - w <= i <= stations[idx] + w:
            i = stations[idx] + w + 1
            idx += 1
        else:
            answer += 1
            i += cover
            
    return answer