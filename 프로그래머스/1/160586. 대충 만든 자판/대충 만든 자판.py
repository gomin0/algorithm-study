def solution(keymap, targets):
    answer = []
    char_to_press = {}
    
    # 각 문자에 대한 최소 키 누름 횟수를 미리 계산
    for key in keymap:
        for i, char in enumerate(key):
            if char not in char_to_press or i + 1 < char_to_press[char]:
                char_to_press[char] = i + 1

    for target in targets:
        count = 0
        for char in target:
            if char not in char_to_press:
                count = -1
                break
            count += char_to_press[char]
        answer.append(count)

    return answer