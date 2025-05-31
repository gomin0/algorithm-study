def solution(s):
    count: int = 0
    time: int = 0
    while s != '1':
        length: int = len(s)
        c: int = s.count('1')
        count += length - c
        s: str = '1' * count
        s: str = format(c, 'b')
        time += 1
    
    return [time, count]