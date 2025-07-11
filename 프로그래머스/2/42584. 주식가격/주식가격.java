import java.util.*;

class Solution {
    public int[] solution(int[] prices) {
        int len = prices.length;
        int[] answer = new int[len];
        Stack<Integer> stack = new Stack<>();
        
        for (int i=0; i<len; i++) {
            while (!stack.isEmpty() && prices[i] < prices[stack.peek()]) {
                int idx = stack.pop();
                answer[idx] = i - idx;
            }
            stack.push(i);
        }
        
        // 끝까지 가격이 떨어지지 않은 경우
        while (!stack.isEmpty()) {
            int idx = stack.pop();
            answer[idx] = len - idx - 1;
        }
        
        return answer;
    }
}