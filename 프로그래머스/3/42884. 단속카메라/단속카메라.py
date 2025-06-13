def solution(routes):
    answer: int = 1
    routes.sort(key=lambda x: x[1])
    camera_point: int = routes[0][1]
    
    for i in range(1, len(routes)):
        start: int
        end: int
        start, end = routes[i]
        
        if camera_point < start:
            answer += 1
            camera_point = end
    
    return answer