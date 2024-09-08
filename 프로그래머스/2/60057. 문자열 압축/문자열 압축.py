def solution(s):
    answer = float('inf')
    
    length = len(s)
    
    # 이거 처리 안하면 테스트 5에서 런타임 에러
    if length == 1:
        return 1
    
    for part in range(1, length // 2 + 1):
        result = ""
        first = s[:part]
        count = 1
        
        for i in range(part, len(s), part):
            if s[i:i+part] == first:
                count += 1
            else:
                if count > 1:
                    result += str(count) + first # 반복 수 + 반복 문자
                else:
                    result += first # 그대로
                first = s[i:i+part]
                count = 1
        
        # 마지막 부분
        if count > 1:
            result += str(count) + first # 반복 수 + 반복 문자
        else:
            result += first # 그대로
            
        answer = min(answer, len(result))
        
    
    return answer