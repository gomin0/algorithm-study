class Solution {
    public int solution(int n) {
        int answer = 0;
        
        String three = Integer.toString(n, 3);
        String reverseThree = new StringBuilder(String.valueOf(three)).reverse().toString();
        
        answer = Integer.parseInt(reverseThree, 3);  
        
        return answer;
    }
}