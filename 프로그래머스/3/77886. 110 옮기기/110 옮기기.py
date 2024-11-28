def solution(s):
    answer = []
    
    for string in s:
        count110 = 0
        stack = []
        
        # 문자열을 한 번 순회하면서 "110"을 제거하고 그 개수를 센다
        i = 0
        while i < len(string):
            if string[i] == '0':
                # stack의 끝에 "110"이 있다면 제거하고 count를 증가시킵니다.
                if len(stack) >= 2 and stack[-2] == '1' and stack[-1] == '1':
                    stack.pop()
                    stack.pop() # 11 제거 -> 110 빼기
                    count110 += 1
                    i += 1
                else:
                    stack.append(string[i])
                    i += 1
            else:
                stack.append(string[i])
                i += 1
                
        stack = ''.join(stack)
        idx = stack.rfind('0')
        # "110" 삽입
        if idx != -1:  # find함수는 없으면 -1 반환
            new_string = stack[:idx+1] + '110' * count110 + stack[idx+1:]
        else:
            new_string = '110' * count110 + stack
        answer.append(new_string)
    
    return answer
