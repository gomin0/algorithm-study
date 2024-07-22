def solution(id_list, report, k):
    answer = []
    report_list = {user: set() for user in id_list}
    report_count = {user: 0 for user in id_list}
    baned = []
    
    for i in report:
        reporter, reported = i.split(" ")
        if reported not in report_list[reporter]:
            report_list[reporter].add(reported)
            report_count[reported] += 1
            
    for user, count in report_count.items():
        if count >= k:
            baned.append(user)
            
    mail = {user: 0 for user in id_list}
    for a in id_list:
        for b in report_list[a]:
            if b in baned:
                mail[a] += 1
                
    for k in id_list:
        answer.append(mail[k])
            
    return answer