def solution(s):
    answer = 0
    
    x = s[0]
    same = 0
    differ = 0
    
    for idx, value in enumerate(s):
        if idx == len(s) - 1:
            answer += 1
            break
        if value == x:
            same += 1
        else:
            differ += 1
        if same == differ and same != 0:
            answer += 1
            x = s[idx + 1]
            same = 0
            differ = 0
    
    return answer