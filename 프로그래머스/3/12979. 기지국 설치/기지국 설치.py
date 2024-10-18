def solution(n, stations, w):
    answer = 0
    
    position = 1
    cover = 2 * w + 1
    
    for station in stations:
        if position < station - w:
            gap = station - w - position
            answer += (gap + cover - 1) // cover
            
        position = station + w + 1
        
    if position <= n:
        gap = n - position + 1
        answer += (gap + cover - 1) // cover
    
    return answer