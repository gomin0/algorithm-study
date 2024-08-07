# 아으 모르겠다 heapq O(logn) 최소 힙에서 제일 앞에값은 항상 최소값(정렬은 아님)
import heapq

def solution(scoville, K):
    # 주어진 리스트를 힙으로 변환
    heapq.heapify(scoville)
    answer = 0
    
    while True:
        minscov = heapq.heappop(scoville) # 가장 작은거 pop 됨
        if minscov >= K:
            break
        if len(scoville) <= 0:
            return -1
        minscov2 = heapq.heappop(scoville)
        heapq.heappush(scoville, minscov + minscov2 * 2)
        answer += 1
    
    return answer



# O(n^2)
# def solution(scoville, K):
#     answer = 0
    
#     while True:
        
#         idx = 0
#         for i in range(1, len(scoville)):
#             if scoville[i] < scoville[idx]:
#                 idx = i
#         minscov = scoville.pop(idx)
        
#         if minscov >= K:
#             break
            
#         if len(scoville) <= 0:
#             return -1
        
#         idx2 = 0
#         for j in range(1, len(scoville)):
#             if scoville[j] < scoville[idx2]:
#                 idx2 = j
#         minscov2 = scoville.pop(idx2)
        
#         scoville.append(minscov + minscov2 * 2)
#         answer += 1
        
#     return answer


# O(nlogn)
# 효율성 시간 초과 정렬은 O(nlogn)
# def solution(scoville, K):
#     answer = 0
#     scoville.sort(reverse = True)
    
#     while scoville[-1] < K:
#         if len(scoville) <= 1:
#             return -1
#         minscov = scoville.pop()
#         minscov2 = scoville.pop()
#         scoville.append(minscov + minscov2 * 2)
#         answer += 1
#         scoville.sort(reverse = True)
    
#     return answer