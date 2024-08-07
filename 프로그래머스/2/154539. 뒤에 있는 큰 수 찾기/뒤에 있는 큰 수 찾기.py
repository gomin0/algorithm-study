def solution(numbers):
    length = len(numbers)
    answer = [-1] * len(numbers)
    stack = []
    
    for i in range(length - 1, -1, -1):
        while stack and stack[-1] <= numbers[i]:
            stack.pop()
        if stack:
            answer[i] = stack[-1]
        stack.append(numbers[i])
    
    return answer


# 시간초과
# def solution(numbers):
#     answer = []
    
#     for i in range(len(numbers)):
#         big = False
#         for j in range(i, len(numbers)):
#             if numbers[i] < numbers[j]:
#                 big = True
#                 answer.append(numbers[j])
#                 break
#         if not big:
#             answer.append(-1)
    
#     return answer