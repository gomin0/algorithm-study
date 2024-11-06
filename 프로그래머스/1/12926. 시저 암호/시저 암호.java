class Solution {
    public String solution(String s, int n) {
        StringBuilder answer = new StringBuilder();
        
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            
            if (c == ' ') {
                answer.append(c);
            }
            else if (Character.isUpperCase(c)) {
                answer.append((char)((c - 'A' + n) % 26 + 'A'));
            }
            else if (Character.isLowerCase(c)) {
                answer.append((char)((c - 'a' + n) % 26 + 'a'));
            }
        }
        
        return answer.toString();
    }
}