def solution(s):
    answer = []

    for string in s:
        stack = []
        count = 0

        for c in string:
            stack.append(c)
            if len(stack) >= 3 and stack[-3:] == ['1', '1', '0']:
                stack.pop()
                stack.pop()
                stack.pop()
                count += 1

        idx = len(stack)
        for i in range(len(stack) - 1, -1, -1):
            if stack[i] == '0':
                idx = i + 1
                break
        else:
            idx = 0

        result = stack[:idx] + ['110'] * count + stack[idx:]
        answer.append(''.join(result))

    return answer
