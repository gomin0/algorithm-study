# 그냥 작은 자리수 부터 처리
def solution(storey):
    answer = 0
    
    while storey:
        remain = storey % 10
        next_remain = (storey // 10) % 10
        
        if remain > 5 or (remain == 5 and next_remain >= 5): # 5일때 다음 숫자가 5보다 크면 올리는게 이득 작으면 내리는게 이득
            answer += 10 - remain # 올리기
            storey += 10
        else:
            answer += remain
            
        storey //= 10
    
    return answer


# def solution(storey):
#     answer = 0
    
#     length = len(str(storey))
    
#     for i in range(length-1, -1, -1):
#         temp = 0 # 9인 경우에 대한 처리
#         div = 10 ** i
#         share = storey // div
#         storey -= div * share
        
#         if share > 5: # 위로 올리고 한번에 내리기
#             if share == 9:
#                 temp = (10 - share) + 1
#                 break
#             answer += (10 - share) + 1
#         else: # 내리기
#             answer += share
#             answer += temp
#             temp = 0
            
#     if temp != 0:
#         answer += temp
        
#     return answer