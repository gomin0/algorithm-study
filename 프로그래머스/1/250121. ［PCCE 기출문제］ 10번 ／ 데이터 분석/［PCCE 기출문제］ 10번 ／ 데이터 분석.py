def solution(data, ext, val_ext, sort_by):
    answer = []
    
    extract = {"code": 0, "date": 1, "maximum": 2, "remain": 3}
    
    for i in data:
        if i[extract[ext]] < val_ext:
            answer.append(i)
    
    result = sorted(answer, key=lambda x: x[extract[sort_by]])
    
    return result