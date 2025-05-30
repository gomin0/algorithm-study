def solution(s):
    answer: str = ""
    words: list[str] = s.split(" ")
    for word in words:
        if not word:
            answer += " "
            continue
        answer += word[0].upper() + word[1:].lower() + " "
        
    return answer[:-1]