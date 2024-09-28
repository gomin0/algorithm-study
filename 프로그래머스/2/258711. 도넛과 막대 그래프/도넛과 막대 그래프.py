from collections import defaultdict

def solution(edges):
    
    edge_counts = defaultdict(lambda: [0, 0])  # edge: [나가는 수, 들어오는 수]
    for a, b in edges:
        edge_counts[a][0] += 1  # 나가는 수 증가
        edge_counts[b][1] += 1  # 들어오는 수 증가

    generated = 0
    donut = 0
    stick = 0
    eight = 0
    for key, (out_count, in_count) in edge_counts.items():
        if out_count >= 2 and in_count == 0:  # 나가는 수가 2이상, 들어어는 건 없는경우
            generated = key
        elif out_count == 0 and in_count > 0:  # 나가는 거는 있는데 들어오는게 없어(생성된거 제외)
            stick += 1
        elif out_count >= 2 and in_count >= 2:
            eight += 1
    donut = edge_counts[generated][0] - stick - eight
    
    return [generated, donut, stick, eight]