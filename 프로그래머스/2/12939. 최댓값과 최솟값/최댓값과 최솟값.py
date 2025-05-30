def solution(s):
    nums: list[int] = [int(n) for n in s.split(" ")]
        
    answer: str = str(min(nums)) + " " + str(max(nums))
    return answer