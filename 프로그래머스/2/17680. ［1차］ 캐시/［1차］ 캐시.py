def solution(cacheSize, cities):
    answer = 0
    
    cache = []
    if cacheSize == 0:
        return len(cities) * 5
    
    cities = [city.lower() for city in cities]
    
    for i in cities:
        if i in cache:
            cache.remove(i)
            answer += 1
        else:
            if len(cache) >= cacheSize:
                cache.remove(cache[0])
            answer += 5
        cache.append(i)
            
    
    return answer