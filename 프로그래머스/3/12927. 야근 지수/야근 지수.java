import java.util.*;

class Solution {
    public long solution(int n, int[] works) {
        PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());
        for (int work : works) pq.offer(work);
        
        long answer = 0;
        while (n > 0 && !pq.isEmpty()) {
            int maxWork = pq.poll();
            maxWork--;
            if (maxWork > 0) pq.offer(maxWork);
            n--;
        }
        
        while (!pq.isEmpty()) {
            int remain = pq.poll();
            answer += remain * remain;
        }
        
        return answer;
    }
}