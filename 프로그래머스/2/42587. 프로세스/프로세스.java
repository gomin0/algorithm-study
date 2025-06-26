import java.util.*;

class Solution {
    public int solution(int[] priorities, int location) {
        Queue<Integer> queue = new ArrayDeque<>();
        PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());
        for (int priority : priorities) {
            queue.offer(priority);
            pq.offer(priority);
        }
        
        int answer = 0;
        int max_p = pq.poll();
        while (!queue.isEmpty()) {
            int p = queue.poll();
            if (max_p == p) {
                answer++;
                if (location == 0)
                    return answer;
                max_p = pq.poll();
                location--;
            }
            else {
                queue.offer(p);
                if (location == 0)
                    location = queue.size() - 1;
                else
                    location--;
            }
        }
        return answer;
    }
}