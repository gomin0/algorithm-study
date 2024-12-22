def check(string, left, right):
    n = len(string)
    while 0 <= left and right < n and string[left] == string[right]:
        left -= 1
        right += 1
    return right - left - 1  # 한단계 더 +- 됐으니까

def solution(s):
    answer = 0

    for i in range(len(s)):
        len1 = max(answer, check(s, i, i))
        len2 = max(answer, check(s, i, i+1))
        answer = max(answer, len1, len2)
        
    return answer