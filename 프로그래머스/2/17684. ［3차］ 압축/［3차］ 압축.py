def solution(msg):
    answer = []
    dict_zip = {}
    
    for i in range(26):
        dict_zip[chr(65 + i)] = i+1
    number = 27
    
    # while msg 이렇게 하고 msg.pop(0) 이렇게 하려고 했는데 문자열은 pop을 못써서 idx로
    idx = 0
    while idx < len(msg):
        
        word = msg[idx]
        idx += 1
        
        while idx < len(msg) and (word + msg[idx]) in dict_zip:
            word += msg[idx]
            idx += 1
        
        if idx < len(msg):
            dict_zip[word + msg[idx]] = number
            number += 1
        answer.append(dict_zip[word])
        
    return answer