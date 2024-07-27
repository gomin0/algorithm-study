def solution(n, words):
    answer = []
    prev_words = []
    
    end = words[0][-1]
    prev_words.append(words[0])
    
    for i in range(1, len(words)):
        player = (i % n) + 1
        turn = (i // n) + 1
        if not words[i].startswith(end) or words[i] in prev_words:
            return [player, turn]
        end = words[i][-1]
        prev_words.append(words[i])

    return [0, 0]