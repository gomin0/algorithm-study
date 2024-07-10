def solution(answers):

    result = []
    no1 = [1, 2, 3, 4, 5]
    no2 = [2, 1, 2, 3, 2, 4, 2, 5]
    no3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    scores = [0, 0, 0]
    
    for i in range(len(answers)):
        if answers[i] == no1[i % len(no1)] :
            scores[0] += 1
        if answers[i] == no2[i % len(no2)] :
            scores[1] += 1
        if answers[i] == no3[i % len(no3)] :
            scores[2] += 1
    
    max_score = max(scores)
    print(scores)
    print(max_score)
    
    for i in range(len(scores)):
        if scores[i] == max_score:
            result.append(i + 1)
    
    return result