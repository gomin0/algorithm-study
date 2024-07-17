def solution(new_id):
    answer = ''
    two_id = ''

    # 1단계
    new_id = new_id.lower()
    # 2단계
    for i in new_id:
        if i.isalpha() or i.isdigit() or i in ["-", "_", "."]:
            two_id += i
    # 3단계
    prev_char = ''
    for char in two_id:
        if char == '.' and prev_char == '.':
            continue
        answer += char
        prev_char = char
    # 4단계
    if len(answer) > 0 and answer[0] == '.':
        answer = answer[1:]
    if len(answer) > 0 and answer[-1] == '.':
        answer = answer[:-1]
    # 5단계
    if len(answer) == 0:
        answer += "a"
    # 6단계
    if len(answer) > 15:
        if answer[14] == '.':
            answer = answer[:14]
        else:
            answer = answer[:15]
    # 7단계
    last_word = answer[-1]
    while len(answer) <= 2:
        answer += last_word
        
    return answer