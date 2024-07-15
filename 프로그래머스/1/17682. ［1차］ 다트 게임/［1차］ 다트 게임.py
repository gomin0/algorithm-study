def solution(dartResult):
    answer = []
    
    score = ''
    for i in dartResult:
        if i.isdigit():
            score += i
        elif i == 'S':
            answer.append(int(score))
            score = ''
        elif i == 'D':
            score = pow(int(score), 2)
            answer.append(score)
            score = ''
        elif i == 'T':
            score = pow(int(score), 3)
            answer.append(score)
            score = ''
        elif i == '*':
            if len(answer) > 1:
                answer[-2] *= 2
                answer[-1] *= 2
            else:
                answer[-1] *= 2
        elif i == '#':
            answer[-1] *= -1
    
    return sum(answer)