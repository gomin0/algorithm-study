def solution(s):
    answer = ''
    s_num = [int(x) for x in s.split()]

    answer = str(min(s_num)) + " " + str(max(s_num))

    
    return answer