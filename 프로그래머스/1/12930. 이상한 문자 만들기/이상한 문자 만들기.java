class Solution {
    public String solution(String s) {
        String answer = "";
        int count = 0;
        
        for (int i = 0; i < s.length(); i++) {
            char alpha = s.charAt(i);
            if (alpha == ' ') {
                answer += ' ';
                count = 0;
                continue;
            }
            
            if (count % 2 == 0) {
                answer += Character.toUpperCase(alpha);
            }
            else {
                answer += Character.toLowerCase(alpha);
            }
            count ++;
        }
        
        return answer;
    }
}