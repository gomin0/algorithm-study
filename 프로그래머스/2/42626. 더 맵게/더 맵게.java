import java.util.*;

class Solution {
    public int solution(int[] scoville, int K) {        
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        int answer = 0;
        
        for(int i : scoville) {
            pq.add(i);
        }
        
        while (pq.peek() < K) {
            if (pq.size() < 2) {
                return -1;
            }
            int a = pq.poll();
            int b = pq.poll();
            int mix = a + (b*2);
            pq.add(mix);
            answer++;
        }
        
        return answer;
    }
}