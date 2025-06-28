import java.util.*;

class Solution {
    public int solution(int[] numbers, int target) {
        int answer = 0;
        Stack<int[]> stack = new Stack<>();
        stack.push(new int[]{0, 0}); //{depth, num}
        int len = numbers.length;
        
        while (!stack.isEmpty()) {
            int[] current = stack.pop();
            int depth = current[0];
            int num = current[1];
            if (depth == len) {
                if (num == target)
                    answer++;
                continue;
            }
            stack.push(new int[]{depth+1, num+numbers[depth]});
            stack.push(new int[]{depth+1, num-numbers[depth]});
        }
        return answer;
    }
}