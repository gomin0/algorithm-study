import java.util.*;

class Solution {
    public int solution(int k, int m, int[] score) {
        int answer = 0;
        
        Arrays.sort(score);
        
        for (int i = score.length-1; i > -1; i -= m) {
            if (i-m+1 > -1) {
            	answer += score[i - m + 1] * m;
            }
        }
        
        return answer;
    }
}