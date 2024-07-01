def solution(food):
    answer = ''
    
    for i in range(1, len(food)):
        for _ in range(food[i] // 2):
            answer += str(i)
            
    reverse = ''.join(reversed(answer))  # 문자열 뒤집기
    answer += '0'
    answer += reverse
        
    return answer