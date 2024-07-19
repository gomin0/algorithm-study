def solution(today, terms, privacies):
    answer = []
    type_of_word = {}
    
    today_day = today.split('.')
            
    sum_today = (int(today_day[0]) - 1) * 12 * 28 + int(today_day[1]) * 28 + int(today_day[2])
    
    for term in terms:
        word_type, duration = term.split()
        type_of_word[word_type] = int(duration)
        
    for index, i in enumerate(privacies, 1):
        date, alpha_type = i.split()
        day = date.split('.')
        sum_day = (int(day[0]) - 1) * 12 * 28 + int(day[1]) * 28 + int(day[2])
        if sum_day + type_of_word[alpha_type] * 28 <= sum_today:
            answer.append(index)
            
    return answer