def solution(X, Y):
    result = ""
    answer = []
    
    count_X = [0] * 10
    count_Y = [0] * 10
    
    for a in X:
        count_X[int(a)] += 1
    for b in Y:
        count_Y[int(b)] += 1
            
    for i in range(len(count_X) - 1, -1, -1):
        if count_X[i] != 0 and count_Y[i] != 0:
            for _ in range(min(count_X[i], count_Y[i])):
                answer.append(str(i))
    
    if answer == []:
        return "-1"
    
    result = "".join(answer)
    
    if result[0] == "0":
        return "0"
    
    return result