def solution(fees, records):
    answer = []
    record_dict = {}
    
    for i in records:
        a, b, c = i.split(" ")
        if b in record_dict:
            record_dict[b].append((a, c))
        else:
            record_dict[b] = []
            record_dict[b].append((a, c))
    
    
    record_dict = dict(sorted(record_dict.items()))
    
    for j in record_dict:
        time = 0
        idx = 0
        if len(record_dict[j]) % 2 != 0:
            time += 1439 # 23:59
        for k in range(len(record_dict[j])):
            d, e = record_dict[j][k]
            h, m = d.split(":")
            #분으로 바꿔
            if idx % 2 == 0: # 들어온 시간 빼기
                time -= int(h) * 60 + int(m)
            else: # 나간 시간 더하기
                time += int(h) * 60 + int(m)
            idx += 1
        if time < fees[0]:
            answer.append(fees[1])
        elif (time - fees[0]) % fees[2] != 0:
            answer.append(fees[1] + ((time - fees[0]) // fees[2] + 1) * fees[3])
        else:
            answer.append(fees[1] + ((time - fees[0]) // fees[2]) * fees[3])
            
    return answer