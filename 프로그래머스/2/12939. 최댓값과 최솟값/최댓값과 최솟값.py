def solution(s):
    nums: list[int] = [int(n) for n in s.split(" ")]
    max_num: int = max(nums)
    min_num: int = min(nums)
        
    answer: str = str(min_num) + " " + str(max_num)
    return answer