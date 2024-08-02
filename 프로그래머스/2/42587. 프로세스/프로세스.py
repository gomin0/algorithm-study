def solution(priorities, location):
    answer = 0
    
    while priorities:
        now_max = max(priorities)
        if priorities[0] < now_max:
            priorities.append(priorities.pop(0))
            if location == 0:
                location = len(priorities) - 1
            else:
                location -= 1
        else:
            answer += 1
            if location == 0:
                return answer
            else:
                location -= 1
            priorities.pop(0)
    
    return answer