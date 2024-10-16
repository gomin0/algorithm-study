class Solution {
    public String solution(String phone_number) {
        String answer = "";
        int length = phone_number.length();
        
        for (int i = 0; i < length - 4; i++) {
            answer += '*';
        }
        
        for (int i = length - 4; i < length; i++) {
            answer += phone_number.charAt(i);
        }
        
        return answer;
    }
}