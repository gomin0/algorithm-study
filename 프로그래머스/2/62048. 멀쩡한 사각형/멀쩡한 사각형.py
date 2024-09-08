import math

def solution(w,h):
    answer = w * h
    
    multiple = math.gcd(w, h)
    
    mw = w // multiple
    mh = h // multiple
    
    answer -= (mh + mw - 1) * multiple
    
    return answer