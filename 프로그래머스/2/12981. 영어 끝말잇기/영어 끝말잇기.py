def solution(n, words):
    answer = [0, 0]
    
    prev_words: set[str] = set()
    end_word: str = words[0][-1]
    prev_words.add(words[0])
    for i in range(1, len(words)):
        word: str = words[i]
        if word in prev_words or not word.startswith(end_word):
            answer[0] = i % n + 1
            answer[1] = i // n + 1
            break
        prev_words.add(word)
        end_word = word[-1]

    return answer