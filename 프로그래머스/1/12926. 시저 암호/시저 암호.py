def solution(s, n):
    answer = ''
    
    for char in s:
        if char.islower(): # 소문자인 경우
            new_char = chr((ord(char) - ord('a') + n) % 26 + ord('a'))
            answer += new_char
        elif char.isupper():  # 대문자인 경우
            new_char = chr((ord(char) - ord('A') + n) % 26 + ord('A'))
            answer += new_char
        else: #공백인 경우
            answer += ' '
    
    return answer