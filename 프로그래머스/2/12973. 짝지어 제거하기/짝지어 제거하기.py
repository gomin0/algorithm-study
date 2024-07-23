def solution(s):
    answer = 0

    stack = []
    
    for char in s:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)
    
    return 1 if not stack else 0