def solution(s):
    sorted_s = ''.join(sorted(s, reverse=True)) # s는 불변이라 새로 담아야함
    return sorted_s