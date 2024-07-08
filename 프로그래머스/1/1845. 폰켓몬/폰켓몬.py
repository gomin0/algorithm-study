def solution(nums):
    get = []
    
    for i in nums:
        if i not in get:
            get.append(i)
    
    if len(get) < len(nums) / 2:
        return len(get)
    else:
        return len(nums) / 2