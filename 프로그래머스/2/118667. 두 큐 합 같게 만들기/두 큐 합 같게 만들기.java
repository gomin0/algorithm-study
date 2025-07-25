import java.util.*;

class Solution {
    public int solution(int[] queue1, int[] queue2) {
        Queue<Integer> q1 = new LinkedList<>();
        Queue<Integer> q2 = new LinkedList<>();
        int maxChange = 0;
        
        long sum1 = 0;
        for (int num : queue1) {
            sum1 += num;
            q1.offer(num);
            maxChange++;
        }
        long sum2 = 0;
        for (int num: queue2) {
            sum2 += num;
            q2.offer(num);
            maxChange++;
        }
        long sum = sum1 + sum2;
        if (sum % 2 != 0)
            return -1;
        sum /= 2;
        maxChange *= 2;
        
        int answer = 0;
        while (answer < maxChange) {
            if (sum1 == sum) {
                return answer;
            }
            else if (sum1 > sum) {
                int num = q1.poll();
                q2.offer(num);
                sum1 -= num;
            }
            else {
                int num = q2.poll();
                q1.offer(num);
                sum1 += num;
            }
            answer++;
        }
        
        return -1;
    }
}