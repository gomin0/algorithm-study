def solution(s):
    answer = []
    # 많이 나온 순으로 배열에 담기면 되겠다
    num_count = {}
    
    num = ''
    for i in range(1, len(s)):
        if s[i].isdigit():
            num += s[i]
        elif s[i] == ',' or s[i] == '}':
            if s[i - 1].isdigit():
                if num in num_count:
                    num_count[num] += 1
                else:
                    num_count[num] = 1
            num = ''
            
    answer = [int(k) for k, v in sorted(num_count.items(), key=lambda item: item[1], reverse=True)]
    
    return answer