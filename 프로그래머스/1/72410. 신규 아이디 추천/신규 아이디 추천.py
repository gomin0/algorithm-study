def solution(new_id):
    answer = ''
    two_id = ''

    # 1단계
    new_id = new_id.lower()
    # 2단계
    for i in new_id:
        if i.isalpha() or i.isdigit() or i in ["-", "_", "."]:
            answer += i
    # 3단계
    # prev_char = ''
    # for char in two_id:
    #     if char == '.' and prev_char == '.':
    #         continue
    #     answer += char
    #     prev_char = char
    while '..' in answer:
        answer = answer.replace('..', '.')
    # 4단계
    if len(answer) > 0 and answer[0] == '.':
        answer = answer[1:]
    if len(answer) > 0 and answer[-1] == '.':
        answer = answer[:-1]
    # 5단계
    if len(answer) == 0:
        answer = "a"
    # 6단계
    if len(answer) > 15:
        if answer[14] == '.':
            answer = answer[:14]
            # 이랬는데 뒤에 또 .이면 어캄?
        else:
            answer = answer[:15]
    # 7단계
    while len(answer) <= 2:
        answer += answer[-1]
        
    return answer