# deque 활용 O(n)
# 모든 k길이 구간별 최댓값 중 최소값 구하기
from collections import deque

def solution(stones, k):
    n = len(stones)
    queue = deque()
    answer = float('inf')
    
    for i in range(n):
        # 뒤에서부터 현재 값보다 작은 값을 제거
        while queue and queue[-1][1] < stones[i]:
            queue.pop()
        
        queue.append((i, stones[i]))
        
        if queue[0][0] <= i - k:
            queue.popleft()
            
        if i >= k - 1:
            answer = min(answer, queue[0][1])
        # print(i, queue[0][1])
            
    return answer



# # 이분 탐색
# def solution(stones, k):
#     left = 0
#     right = max(stones)
    
#     while left <= right:
#         mid = (left + right) // 2
#         possible = True
        
#         count = 0
#         for stone in stones:
#             if stone < mid:
#                 count += 1
#                 if count >= k:
#                     possible = False
#                     break
#             else:
#                 count = 0    
        
#         if possible:
#             left = mid + 1
#         else:
#             right = mid - 1
        
#     return mid