def solution(k, score):
    answer = []
    crown = []
    
    for i in score:
        if len(crown) < k:
            crown.append(i)
        else:
            min_crown = min(crown)
            if i > min_crown:
                crown.remove(min_crown)
                crown.append(i)
        answer.append(min(crown))
    return answer