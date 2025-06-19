import java.util.*;

class Solution {
    public List<Integer> solution(int[] progresses, int[] speeds) {
        List<Integer> answer = new ArrayList<>();
        Queue<Integer> queue = new ArrayDeque<>();
        
        // queue에 남은 일수 저장
        for (int i = 0; i < progresses.length; i++) {
            int days = (100 - progresses[i] + speeds[i] - 1) / speeds[i];
            queue.offer(days);
        }
        
        // while 문 안에 while 문이 있지만 실제로는 한번씩만 접근해서 O(n)
        while (!queue.isEmpty()) {
            int current = queue.poll();
            int count = 1;
            
            while (!queue.isEmpty() && queue.peek() <= current) {
                queue.poll();
                count++;
            }
            answer.add(count);
        }
        
        return answer;
    }
}