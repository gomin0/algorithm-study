def solution(participant, completion):
    
    participant.sort()
    completion.sort()
    
    for i, j in zip(participant, completion):
        if i != j:
            return i
    
    return participant[-1]
    
    #시간 초과
#     for i in completion:
#         participant.remove(i)
    
#     return participant[0]