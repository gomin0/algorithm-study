from collections import defaultdict

def solution(genres, plays):
    answer = []
    
    genre_plays = defaultdict(int)
    play_genres = defaultdict(list)
    
    for i in range(len(genres)):
        genre_plays[genres[i]] += plays[i]
        play_genres[genres[i]].append((i, plays[i]))
        
    sorted_genres = sorted(genre_plays.items(), key=lambda x: x[1], reverse = True)
    
    for genre, times in sorted_genres:
        sorted_song = sorted(play_genres[genre], key=lambda x: (-x[1], x[0]))
        
        for i, time in sorted_song[:2]:
            answer.append(i)
    
    return answer