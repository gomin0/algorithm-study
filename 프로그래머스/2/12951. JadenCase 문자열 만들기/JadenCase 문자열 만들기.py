def solution(s):
    answer = ''
    
    for i in range(len(s)):
        if i == 0 or s[i - 1] == ' ':
            answer += s[i].upper() if s[i].isalpha() else s[i]
        else:
            answer += s[i].lower() if s[i].isalpha() else s[i]
            
    return answer