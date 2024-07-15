def solution(babbling):

    answer = 0
    speek = ["aya", "ye", "woo", "ma"]
    
    for b in babbling:
        if "ayaaya" in b or "yeye" in b or "woowoo" in b or "mama" in b:
            continue    
        if not b.replace("aya", " ").replace("ye", " ").replace("woo", " ").replace("ma", " ").replace(" ", ""):
            answer += 1
    return answer

#     for word in babbling:
#         speeking = 0
#         valid = True
        
#         while speeking < len(word):
#             matched = False
#             for sound in speek:
#                 if word.startswith(sound, speeking) and not word.startswith(sound * 2, speeking):
#                     speeking += len(sound)
#                     matched = True
#                     break
#             if not matched:
#                 valid = False
#                 break
        
#         if valid:
#             answer += 1
