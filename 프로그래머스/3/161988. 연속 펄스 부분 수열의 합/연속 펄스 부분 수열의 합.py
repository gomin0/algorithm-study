def solution(sequence) -> int:
    length: int = len(sequence)
    pulse1: list[int] = [
        sequence[i] if i % 2 == 0 else -sequence[i] for i in range(length)
    ]
    pulse2: list[int] = [
        sequence[i] if i % 2 != 0 else -sequence[i] for i in range(length)
    ]
    
    def max_sub_sum(nums) -> int:
        max_sum: int = nums[0]
        current_sum: int = nums[0]
        
        for i in range(1, len(nums)):
            num: int = nums[i]
            current_sum = max(num, current_sum + num)
            max_sum = max(max_sum, current_sum)
        return max_sum
    
    answer: int = max(max_sub_sum(pulse1), max_sub_sum(pulse2))
    
    return answer