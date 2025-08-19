import java.util.*;

class Solution {
    public int[] solution(int n, long k) {
        List<Integer> numbers = new ArrayList<>();
        for (int i = 1; i <= n; i++) 
            numbers.add(i);
        
        int[] answer = new int [n];
        long[] facto = new long[n+1];
        facto[0] = 1;
        for (int i = 1; i <= n; i++) {
            facto[i] = facto[i-1] * i;
        }
        
        k--;
        for (int i = 0; i < n; i++) {
            long size = facto[n-1-i];
            int idx = (int)(k/size);
            answer[i] = numbers.get(idx);
            numbers.remove(idx);
            k %= size;
        }
        
        return answer;
    }
}