import heapq

def solution(food_times, k):
    if sum(food_times) <= k:
        return -1
    
    n = len(food_times)
    food = []
    for i, food_time in enumerate(food_times):
        heapq.heappush(food, (food_time, i+1))
    
    prev = 0
    while food:
        time = food[0][0]
        diff = time - prev
        if diff == 0:
            heapq.heappop(food)
            n -= 1
            continue
        
        need = n * diff
        if need <= k:
            k -= need
            prev = time
            heapq.heappop(food)
            n -= 1
        else:
            food.sort(key=lambda x : x[1])
            return food[k % n][1]