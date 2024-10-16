class Solution {
    public String solution(String s) {
        String answer = "";
        
        int length = s.length();
        int middle = length/2;
        if (length % 2 == 0) {
            answer += s.charAt(middle - 1);
            answer += s.charAt(middle);
        } else {
            answer += s.charAt(middle);
        }
        
        return answer;
    }
}