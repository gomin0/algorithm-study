import java.util.Stack;

class Solution {
    boolean solution(String s) {
        boolean answer = true;
        Stack<Character> stack = new Stack<>();
        
        for (int i = 0; i < s.length(); i++) {
            char now = s.charAt(i);
            if (now == '(')
                stack.push(now);
            else if (now == ')' && !stack.isEmpty() && stack.pop() == '('){
                continue;
            }
            else {
                answer = false;
                break;
            }
        }

        if (!stack.isEmpty())
            answer = false;
        return answer;
    }
}