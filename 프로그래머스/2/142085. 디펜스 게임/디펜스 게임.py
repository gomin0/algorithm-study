import heapq

def solution(n, k, enemy):
    answer = 0
    max_heap = []
    
    enemies = 0
    
    for i in range(len(enemy)):
        enemies += enemy[i]
        heapq.heappush(max_heap, -enemy[i]) # 최대 힙 사용 위해 음수로 push
        
        if enemies > n:
            if k > 0:
                enemies += heapq.heappop(max_heap) # 가장 큰거의 음수값 더하기
                k -= 1
            else:
                return i
    
    return len(enemy)