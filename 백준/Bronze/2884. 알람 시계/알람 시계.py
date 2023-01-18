h, m = map(int, input().split())

if (m >= 45):
    m -= 45

elif (m < 45 and h >0):
    h -= 1
    m = m + 15
    
else:
    h = 23
    m = m + 15

print(h, m)