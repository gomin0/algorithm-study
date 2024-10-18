def solution(routes):
    answer = 1
    
    routes.sort(key=lambda x: x[1])
    
    idx = 0
    for i in range(1, len(routes)):
        end = routes[idx][1]
        start = routes[i][0]
        if end < start:
            answer += 1
            idx = i
    
    return answer