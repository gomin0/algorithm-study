def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
        
def lcm(a, b):
    return (a * b) / gcd(a, b)

def solution(arr):
    
    least = arr[0]
    for num in arr[1:]:
        least = lcm(least, num)
    answer = 0
    return least