def dictionary(current_word, max_length, alpha, words):
    if len(current_word) > 0:
        words.append(current_word)
    if len(current_word) < max_length:
        for a in alpha:
            dictionary(current_word + a, max_length, alpha, words)

def solution(word):
    answer = 0
    alpha = ['A', 'E', 'I', 'O', 'U']
    words = []
    
    dictionary("", 5, alpha, words)
    
    words.sort()
    
    answer = words.index(word) + 1
    
    return answer