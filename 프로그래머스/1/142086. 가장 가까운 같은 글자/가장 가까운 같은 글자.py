def solution(s):
    last = {}
    answer = []
    
    for i, char in enumerate(s): # enumerate: 요소와 인덱스도 반환
        if char in last:
            closest_index = i - last[char]
        else:
            closest_index = -1
        
        answer.append(closest_index)
        
        last[char] = i
    
    return answer