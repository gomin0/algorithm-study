class Solution {
    public int[] solution(long n) {
        // String numString = String.valueOf(n);
        String numString = Long.toString(n);
        int len = numString.length();
        int[] answer = new int[len];        
        
        for (int i = 0; i < len; i ++) {
            answer[i] = numString.charAt(len-i-1) - '0';
        }
        
        return answer;
    }
}