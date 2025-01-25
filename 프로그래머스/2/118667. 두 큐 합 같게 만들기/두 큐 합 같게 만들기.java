import java.util.*;

class Solution {
    public int solution(int[] queue1, int[] queue2) {
        int answer = 0;
        long sum1 = 0;
        long sum2 = 0;
        Queue<Integer> que1 = new LinkedList<>();
        Queue<Integer> que2 = new LinkedList<>();
        
        for (int q1 : queue1) {
            sum1 += q1;
            que1.offer(q1);
        }
        for (int q2 : queue2) {
            sum2 += q2;
            que2.offer(q2);
        }
        
        long sum = sum1 + sum2;
        if (sum % 2 != 0) {
            return -1;
        }
        
        long goal = sum / 2;
        long maxChange = (queue1.length + queue2.length) * 2;
        
        while (sum1 != goal) {
            
            if (answer > maxChange) {
                return -1;
            }
            
            if (sum1 > goal) {
                int num = que1.poll();
                que2.offer(num);
                sum1 -= num;
            }
            else if (sum1 < goal) {
                int num = que2.poll();
                que1.offer(num);
                sum1 += num;
            }
            answer++;
        }
        
        return answer;
    }
}