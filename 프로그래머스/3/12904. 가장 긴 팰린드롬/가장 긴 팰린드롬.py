def check(string):
    left: int = 0
    right: int = len(string)-1
    while left < right:
        if string[left] == string[right]:
            left += 1
            right -= 1
        else:
            return False
    return True

def solution(s):
    length: int = len(s)
    for l in range(length, 0, -1):
        for i in range(length - l + 1):
            if check(s[i:i+l]):
                return l
    
    return 1