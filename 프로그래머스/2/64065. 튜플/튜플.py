def solution(s):
    answer: list[int] = []
    s = s[2:-2]
    tuple_set: list[str] = s.split("},{")
    result_set: set[int] = set()
    tuple_set.sort(key=len)
    
    for ts in tuple_set:
        numbers: list[str] = ts.split(",")
        for number in numbers:
            num: int = int(number)
            if num not in result_set:
                result_set.add(num)
                answer.append(num)
    
    return answer