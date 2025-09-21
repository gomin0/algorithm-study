import java.util.*;

class Solution {
    public String[] solution(String[] s) {
        String[] answer = new String[s.length];
        
        for (int idx = 0; idx < s.length; idx++) {
            String str = s[idx];
            Stack<Character> stack = new Stack<>();
            int count = 0;
            
            for (char c : str.toCharArray()) {
                stack.push(c);
                if (stack.size() >= 3) {
                    int n = stack.size();
                    if (
                        stack.get(n-3) == '1' &&
                        stack.get(n-2) == '1' &&
                        stack.get(n-1) == '0'
                    ) {
                        stack.pop();
                        stack.pop();
                        stack.pop();
                        count ++;
                    }
                }
            }
            StringBuilder rest = new StringBuilder();
            for (char c : stack) rest.append(c);
            int lastZero = rest.lastIndexOf("0");
            StringBuilder sb = new StringBuilder();
            if (lastZero == -1) {
                for (int i = 0; i < count; i++) sb.append("110");
                sb.append(rest);
            } else {
                sb.append(rest.substring(0, lastZero + 1));
                for (int i = 0; i < count; i++) sb.append("110");
                sb.append(rest.substring(lastZero + 1));
            }
            answer[idx] = sb.toString();
        }
        return answer;
    }
}