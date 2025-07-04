import java.util.*;

class Solution {
    public int[] solution(int[] numbers) {
        int len = numbers.length;
        Stack<Integer> stack = new Stack<>();
        int[] answer = new int[len];
        for (int i = 0; i < len; i++)
            answer[i] = -1;
        
        int idx = len-2;
        stack.push(numbers[len-1]);
        while (idx >= 0) {
            int number = numbers[idx];
            int stackNum = stack.peek();
            if (number < stackNum) {
                answer[idx] = stackNum;
                idx--;
                stack.push(number);
            }
            else {
                stack.pop();
            }
            if (stack.isEmpty()) {
                stack.push(number);
                idx--;
            }
        }
        
        return answer;
    }
}