def solution(clothes):
    answer = 1
    count = {}
    
    for i in clothes:
        if i[1] in count:
            count[i[1]] += 1
        else:
            count[i[1]] = 1
            
    for j in count:
        answer *= count[j] + 1
    
    return answer - 1