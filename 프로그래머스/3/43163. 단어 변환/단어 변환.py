from collections import defaultdict, deque

def can_change(str1, str2):
    count = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            count += 1
        if count > 1:
            return False
    
    return count == 1

def solution(begin, target, words):
    answer = 0
    
    if target not in words:
        return 0
    
    change_dict = defaultdict(list)
    
    def bfs(start, change_dict):
        queue = deque([(start, 0)])
        visited = set([start])
        
        while queue:
            start_str, count = queue.popleft()
            if start_str == target:
                return count
            
            for next_str in change_dict[start_str]:
                if next_str not in visited:
                    queue.append((next_str, count + 1))
                    visited.add(next_str)
    
        return 0
    
    
    for word in words:
        if can_change(begin, word):
            change_dict[begin].append(word)
    
    for i in range(len(words) - 1):
        for j in range(i + 1, len(words)):
            if can_change(words[i], words[j]):
                change_dict[words[i]].append(words[j])
                change_dict[words[j]].append(words[i])
    
    return bfs(begin, change_dict)