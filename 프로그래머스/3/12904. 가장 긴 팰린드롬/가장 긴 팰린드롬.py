

def solution(s):
    answer = 0
    
    def palindrome(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1
    
    for i in range(len(s)):
        len1 = palindrome(i, i)
        len2 = palindrome(i, i + 1)
        answer = max(answer, len1, len2)

    return answer