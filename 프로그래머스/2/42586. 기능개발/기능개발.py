def solution(progresses, speeds):
    answer = []
    length = len(progresses)
    
    deploy = [0] * length
    
    for i in range(length):
        if (100 - progresses[i]) % speeds[i] == 0:
            deploy[i] = int((100 - progresses[i]) / speeds[i])
        else:
            deploy[i] = int((100 - progresses[i]) // speeds[i]) + 1
    
    day = deploy[0]
    count = 1
    for i in range(1, length):
        if deploy[i] <= day:
            count += 1
        else:
            day = deploy[i]
            answer.append(count)
            count = 1
        if i == length-1:
            answer.append(count)
    
    return answer