import math

def solution(arrayA, arrayB):
    answer = 0
    
    lengthA = len(arrayA)
    lengthB = len(arrayB)
    gcdA = arrayA[0]
    gcdB = arrayB[0]
    
    # array길이 2 이상
    if lengthA >= 2:
        for i in range(1, lengthA):
            gcdA = math.gcd(gcdA, arrayA[i])
    if lengthB >= 2:
        for i in range(1, lengthB):
            gcdB = math.gcd(gcdB, arrayB[i])
    
    # a가 될 수 있는지
    aA = True
    aB = True
    
    if gcdA == 1:
        aA = False
    else:
        for b in arrayB:
            if b % gcdA == 0:
                aA = False
    if gcdB == 1:
        aB = False
    else:
        for a in arrayA:
            if a % gcdB == 0:
                aB = False
    
    if not aA and not aB:
        return 0
    elif aA and not aB:
        return gcdA
    elif not aA and aB:
        return gcdB
    else:
        return max(gcdA, gcdB)
    
    return answer