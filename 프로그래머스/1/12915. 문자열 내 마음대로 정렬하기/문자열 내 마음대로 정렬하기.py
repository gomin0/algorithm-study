def solution(strings, n):
    # strings를 n번째 문자를 기준으로 정렬하기
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            # n번째 문자가 같은 경우 사전순으로 정렬
            if strings[i][n] > strings[j][n] or (strings[i][n] == strings[j][n] and strings[i] > strings[j]):
                strings[i], strings[j] = strings[j], strings[i]
    
    return strings