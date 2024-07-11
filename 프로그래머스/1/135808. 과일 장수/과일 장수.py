# k가 굳이 주어진 이유??
def solution(k, m, score):
    answer = 0
    score.sort(reverse=True)
    box = len(score) // m
        
    for i in range(1, box + 1):
        answer += score[i * m - 1] * m
    
    
    return answer