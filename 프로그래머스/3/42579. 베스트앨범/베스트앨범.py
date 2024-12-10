from collections import defaultdict

def solution(genres, plays):
    answer = []
    
    genre_type = len(set(genres))
    genres_plays = defaultdict(int)
    type_music = defaultdict(list)
    for i in range(len(genres)):
        genres_plays[genres[i]] += plays[i]
        type_music[genres[i]].append((i, plays[i]))
        
    sorted_genres = sorted(genres_plays.keys(), key=lambda x: genres_plays[x], reverse = True)
        
    for i in range(genre_type):
        musics = type_music[sorted_genres[i]]
        musics.sort(key=lambda x: x[1], reverse=True)
        answer.append(musics[0][0])
        if len(musics) > 1:
            answer.append(musics[1][0])
    
    return answer