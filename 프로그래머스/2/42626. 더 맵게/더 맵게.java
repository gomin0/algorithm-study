import java.util.*;

class Solution {
    public int solution(int[] scoville, int K) {
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        int answer = 0;
        
        for (int s : scoville)
            pq.add(s);
        
        while (true) {
            if (!pq.isEmpty()) {
                int minScoville = pq.poll();
                if (minScoville >= K)
                    return answer;
                else if (pq.size() >= 1) {
                    int minScoville2 = pq.poll();
                    pq.add(minScoville + minScoville2 * 2);
                    answer++;
                }
                else
                    return -1;
            }
            else
                return -1;
        }
    }
}