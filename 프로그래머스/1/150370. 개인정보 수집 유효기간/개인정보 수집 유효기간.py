def solution(today, terms, privacies):
    answer = []
    
    today_day = [''] * 3
    c = 0
    for a in today:
        if a.isdigit():
            today_day[c] += a
        else:
            c += 1

    type_of_word = {}

    for term in terms:
        word_type, duration = term.split()
        type_of_word[word_type] = int(duration)
            
    sum_today = (int(today_day[0]) - 1) * 12 * 28 + int(today_day[1]) * 28 + int(today_day[2])
        
    for index, i in enumerate(privacies, 1):
        date, alpha_type = i.split()
        day = date.split('.')
        sum_day = (int(day[0]) - 1) * 12 * 28 + int(day[1]) * 28 + int(day[2])
        if sum_day + type_of_word[alpha_type] * 28 <= sum_today:
            answer.append(index)
            
    return answer