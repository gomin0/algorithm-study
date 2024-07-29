def solution(s):
    answer = 0
    
    length = len(s)
    s = s * 2
    
    for i in range(length):
        stack = []
        valid = True
        for j in range(i, i + length):
            if s[j] in '[{(':
                stack.append(s[j])
            elif s[j] in ']})':
                if not stack: # 비어있는 경우
                    valid = False
                    break
                if s[j] == ']' and stack[-1] != '[':
                    valid = False
                    break
                if s[j] == '}' and stack[-1] != '{':
                    valid = False
                    break
                if s[j] == ')' and stack[-1] != '(':
                    valid = False
                    break
                stack.pop()
        
        if valid and not stack:
            answer += 1
    
    return answer

# {(}) 안됨
# def solution(s):
#     answer = 0
#     length = len(s)
#     s = s*2
    
#     for i in range(length):
#         small = 0
#         middle = 0
#         big = 0
#         for j in range(i, i + length):
#             if s[j] == '[':
#                 big += 1
#             elif s[j] == ']':
#                 big -= 1
#             elif s[j] == '{':
#                 middle += 1
#             elif s[j] == '}':
#                 middle -= 1
#             elif s[j] == '(':
#                 small += 1
#             elif s[j] == ')':
#                 small -= 1
#             if big < 0 or middle < 0 or small < 0:
#                 break
#         if big == 0 and middle == 0 and small == 0:
#             answer += 1
    
#     return answer