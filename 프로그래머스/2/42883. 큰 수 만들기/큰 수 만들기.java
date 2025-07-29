import java.util.*;

class Solution {
    public String solution(String number, int k) {
        Stack<Character> stack = new Stack<>();
        
        for (int i = 0; i < number.length(); i++) {
            char num = number.charAt(i);
            while (!stack.isEmpty() && k > 0 && stack.peek() < num) {
                stack.pop();
                k--;
            }
            stack.push(num);
        }
         
        while (k > 0) {
            stack.pop();
            k--;
        }
        
        StringBuilder answer = new StringBuilder();
        for (int i = 0; i < stack.size(); i++) {
            answer.append(stack.get(i));
        }
        return answer.toString();
    }
}