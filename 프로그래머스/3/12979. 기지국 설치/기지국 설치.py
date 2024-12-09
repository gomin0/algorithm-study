def solution(n, stations, w):
    answer = 0

    stations.sort()
    
    idx = 1
    station = 0
    while idx <= n:
        point = stations[station]
        if idx < (point - w):
            answer += 1
            idx += w + w + 1  # i + w 자리에 설치하고 idx 옮기기
        elif (point - w) <= idx <= (point + w):
            idx = point + w + 1
            if station < len(stations) - 1:
                station += 1
        else:
            if station < len(stations) - 1:
                station += 1
                if idx < stations[station]:
                    answer += 1
                    idx += w + w + 1
            else:
                answer += 1
                idx += w + w + 1

    return answer