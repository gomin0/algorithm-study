class Solution {
    boolean solution(String s) {
        boolean answer = true;
        
        int count = 0;
        
        for (int i = 0; i < s.length(); i++) {
            char now = s.charAt(i);
            if (now == '(')
                count += 1;
            
            if (now == ')')
                count -= 1;
            
            if (count < 0) {
                answer = false;
                break;
            }
        }
        
        if (count != 0)
            return false;
        return answer;
    }
}