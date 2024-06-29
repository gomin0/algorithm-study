def solution(s):
    word_to_num = {
        "zero": "0",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }
    
    answer = ''
    temp = ''  # 임시로 영단어를 저장할 문자열
    
    for char in s:
        if char.isdigit():  # 숫자인 경우 answer에 추가
            answer += char
        else:
            temp += char  # 영단어 조각을 임시로 저장
            if temp in word_to_num:  # 만들어진 영단어가 사전에 있는 경우
                answer += word_to_num[temp]  # 숫자로 변환하여 answer에 추가
                temp = ''  # 임시 문자열 초기화
    
    return int(answer)  # answer를 정수형으로 변환하여 반환