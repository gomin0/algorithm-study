def solution(record):
    answer = []
    
    name_dict = {}
    
    for i in record:
        if not i.startswith('Leave'):
            state, uid, name = i.split()
        name_dict[uid] = name

    for i in record:
        if i.startswith('Enter'):
            state, uid, name = i.split()
            answer.append(name_dict[uid]+"님이 들어왔습니다.")
        elif i.startswith('Leave'):
            state, uid = i.split()
            answer.append(name_dict[uid]+"님이 나갔습니다.")
    
    return answer