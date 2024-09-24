def solution(cap, n, deliveries, pickups):
    answer = 0
    delivery = 0
    pickup = 0
    
    for i in range(n - 1, -1, -1):
        delivery += deliveries[i]
        pickup += pickups[i]
        
        while delivery > 0 or pickup > 0:
            delivery -= cap
            pickup -= cap
            answer += (i + 1) * 2
    
    return answer

# def solution(cap, n, deliveries, pickups):
#     road = 0
    
#     delivery_remain = sum(deliveries)
#     pickup_remain = sum(pickups)
    
#     while delivery_remain > 0 or pickup_remain > 0:
#         far = 0  # 가장 멀리가는 거리
#         delivery = 0
#         pickup = 0
        
#         # 가장 멀리 갈 거리 구하기
#         for i in range(n - 1, -1, -1):
#             if deliveries[i] > 0 or pickups[i] > 0:
#                 far = i + 1  # 거리 계산(idx + 1)
#                 break
                
#         # 배달, 수거
#         for i in range(n - 1, -1, -1):
#             if deliveries[i] > 0:
#                 if delivery + deliveries[i] <= cap:
#                     delivery += deliveries[i]
#                     delivery_remain -= deliveries[i]
#                     deliveries[i] = 0
#                 else:
#                     deliveries[i] -= (cap - delivery)
#                     delivery_remain -= (cap - delivery)
#                     delivery = cap
                    
#             if pickups[i] > 0:
#                 if pickup + pickups[i] <= cap:
#                     pickup += pickups[i]
#                     pickup_remain -= pickups[i]
#                     pickups[i] = 0
#                 else:
#                     pickups[i] -= (cap - pickup)
#                     pickup_remain -= (cap - pickup)
#                     pickup = cap
#         road += far * 2 # 왕복    
    
#     return road