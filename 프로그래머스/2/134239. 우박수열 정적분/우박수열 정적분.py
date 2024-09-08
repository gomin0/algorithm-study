def collatz(n):
    count = 0
    spot = []
    spot.append((count, n))
    while n > 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = n * 3 + 1
        count += 1
        spot.append((count, n))
    return spot

def y_value(rain, s):
    value = 0
    for y in range(len(rain)):
        if rain[y][0] == s:
            return rain[y][1]
        elif rain[y][0] > s:
            x1, y1 = rain[y-1][0], rain[y-1][1]
            x2, y2 = rain[y][0], rain[y][1]
            
            inclination = (y2 - y1) / (x2 - x1) # 기울기
            yv = y1 - inclination * x1 # y절편
            
            return inclination * s + yv
    return 0
        

def solution(k, ranges):
    answer = []
    
    rain = collatz(k)
    n = len(rain) - 1
    
    for r in ranges:
        start = r[0]
        end = r[1]
        end += n
        bound = 0
        
        if start > end:
            answer.append(-1)
            continue
        elif start == end:
            answer.append(0)
            continue
            
        for i in range(start, end):
            y_from_s = y_value(rain, i)
            y_to_e = y_value(rain, i + 1)
            
            bound += (y_from_s + y_to_e) * (1 / 2)
        answer.append(bound)
    
    return answer