from collections import defaultdict

def solution(genres, plays):
    total_plays = defaultdict(int)
    genres_play = defaultdict(list)
    n = len(genres)
    for i in range(n):
        total_plays[genres[i]] += plays[i]
        genres_play[genres[i]].append((plays[i], i))
    
    for genre in genres_play:
        genres_play[genre].sort(key = lambda x:(-x[0], x[1]))
    total_genres = []
    for genre in total_plays:
        total_genres.append((total_plays[genre], genre))
    total_genres.sort(reverse = True)
    
    answer = []
    for i in range(len(total_genres)):
        genre = total_genres[i][1]
        count = 0
        for best in genres_play[genre]:
            answer.append(best[1])
            count += 1
            if count == 2:
                break
    
    return answer