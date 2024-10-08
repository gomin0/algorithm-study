import heapq
from collections import defaultdict

def solution(N, road, K):
    answer = 0
    
    graph = defaultdict(list)
    for start, end, time in road:
        graph[start].append((end, time))
        graph[end].append((start, time))
    
    distance = {i: float('inf') for i in range(1, N+1)}
    distance[1] = 0
    
    queue = []
    heapq.heappush(queue, (1, 0)) # (노드, 거리)
    
    while queue:
        now_node, now_distance  = heapq.heappop(queue)
        
        if now_distance > distance[now_node]:
            continue
        
        for next_node, next_distance in graph[now_node]:
            dist = now_distance + next_distance
            if distance[next_node] > dist:
                distance[next_node] = dist
                heapq.heappush(queue, (next_node, dist))
                
    for i in distance.values():
        if i <= K:
            answer += 1
    
    return answer


# # 다익스트라 알고리즘
# import heapq

# def solution(N, road, K):
#     answer = 0
#     INF = float('inf')

#     graph = {i: [] for i in range(1, N+1)}

#     for a,b,c in road:
#         graph[a].append((b, c)) # 출발지에 도착지와 시간 저장
#         graph[b].append((a, c)) # 반대 저장
    
#     distances = {i: INF for i in range(1, N+1)}
    
#     distances[1] = 0
#     queue = [(0, 1)] # (거리, 노드) heapq는 첫번째값(거리) 기준으로 정렬되니까
    
#     while queue:
#         distance, node = heapq.heappop(queue)
        
#         # 현재 노드의 저장된 거리보다 크면 무시
#         if distance > distances[node]:
#             continue
#         # 인접한 노드들에 대한 거리 계산
#         for n, d in graph[node]:
#             dist = distance + d
        
#             # 현재 노드를 거쳐 가는 것이 더 짧으면 업데이트
#             if dist < distances[n]:
#                 distances[n] = dist
#                 heapq.heappush(queue, (dist, n))
    
#     answer = sum(1 for d in distances.values() if d <= K)
    
#     return answer