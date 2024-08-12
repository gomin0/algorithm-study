#병합 정렬 O(nlogn)
def solution(numbers):
    answer = ''
    numbers = list(map(str, numbers))
    
    def merge_sort(arr):
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])
        
        merged = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] + right[j] > right[j] + left[i]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
        
        merged.extend(left[i:])
        merged.extend(right[j:])
        
        return merged

    answer = ''.join(merge_sort(numbers))
    
    return '0' if answer[0] == '0' else answer


# 시간초과
# def solution(numbers):
#     answer = ''
#     numbers = list(map(str, numbers))
#     for i in range(len(numbers) - 1):
#         for j in range(i + 1, len(numbers)):
#             if numbers[i] + numbers[j] < numbers[j] + numbers[i]:
#                 numbers[i], numbers[j] = numbers[j], numbers[i]
    
#     answer = ''.join(numbers)
    
#     if answer[0] == '0':
#         return '0'
    
#     return answer