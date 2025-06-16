from collections import defaultdict

def solution(genres, plays):
    answer: list[int] = []
    genres_plays: defaultdict[str, int] = defaultdict(int)
    genres_history: list[tuple[int, str, int]] = []
    for i in range(len(genres)):
        genres_plays[genres[i]] += plays[i]
        genres_history.append((i, genres[i], plays[i]))
    
    genres_history.sort(key=lambda x: (-x[2], x[0]))
    genres_dict: defaultdict[str, list[int]] = defaultdict(list)
    
    for gh in genres_history:
        idx: int
        genre: str
        play: int
        idx, genre, play = gh
        genres_dict[genre].append(idx)
    
    sorted_genres: list[srt] = sorted(
        genres_plays, 
        key=lambda k: genres_plays[k],
        reverse=True
    )
    
    for genres in sorted_genres:
        idx_in_genres: list[int] = genres_dict[genres]
        answer.append(idx_in_genres[0])
        if len(idx_in_genres) >= 2:
            answer.append(idx_in_genres[1])
    
    return answer