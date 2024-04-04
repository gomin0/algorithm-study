import java.util.*;
class Solution {
    public int[] solution(String[] operations) {
        PriorityQueue<Integer> minq = new PriorityQueue<>();
        PriorityQueue<Integer> maxq = new PriorityQueue<>(Collections.reverseOrder());
        int[] answer = new int[2];
        
        for (String str : operations) {
            StringTokenizer st = new StringTokenizer(str);      
            String a = st.nextToken();
            int value = Integer.parseInt(st.nextToken());
        
            if (minq.size() < 1 && a.equals("D")) {
                continue;
            }
        
            if (a.equals("I")) {
                minq.offer(value);
                maxq.offer(value);
                continue;
            }
        
            if (value < 0) {
                int min = minq.poll();
                maxq.remove(min);
            }
            else {
                int max = maxq.poll();
                minq.remove(max);
            }
        }
        if (minq.size() > 0) {
            answer[0] = maxq.poll();
            answer[1] = minq.poll();
        }      
        
        return answer;
    }
}