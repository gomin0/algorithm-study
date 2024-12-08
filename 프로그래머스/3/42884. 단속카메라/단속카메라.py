def solution(routes):
    answer = 1
    
    routes.sort(key=lambda x: x[1])
    point = routes[0][1]
    
    for i in range(1, len(routes)):
        a, b = routes[i]
        if point < a:
            answer += 1
            point = b
    
    return answer