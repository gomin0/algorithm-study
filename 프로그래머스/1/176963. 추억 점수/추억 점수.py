def solution(name, yearning, photo):
    answer = []
    
    for i in range(len(photo)):
        point = 0
        for j in range(len(photo[i])):
            for k in range(len(name)):
                if photo[i][j] == name[k]:
                    point += yearning[k]
        answer.append(point)
    return answer