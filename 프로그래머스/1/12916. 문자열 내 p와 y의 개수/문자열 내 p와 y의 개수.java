class Solution {
    boolean solution(String s) {
        boolean answer = true;
        int p = 0;
        int y = 0;
        String lower = s.toLowerCase();
        
        for (int i = 0; i < lower.length(); i++) {
            char c = lower.charAt(i);
            if(c == 'p') {
                p++;
            }
            else if(c == 'y') {
                y++;
            }
        }
        
        if (p == y) {
            answer = true;
        }
        else {
            answer = false;
        }

        return answer;
    }
}