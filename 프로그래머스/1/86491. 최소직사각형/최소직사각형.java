import java.util.*;
class Solution {
    public int solution(int[][] sizes) {
        int[] big = new int[sizes.length];
        int[] small = new int[sizes.length];
        int answer = 0;
        for (int i = 0; i < sizes.length; i++) {
            if (sizes[i][0] > sizes[i][1]) {
                big[i] = sizes[i][0];
                small[i] = sizes[i][1];
            }
            else {
                small[i] = sizes[i][0];
                big[i] = sizes[i][1];
            } 
        }
        Arrays.sort(big);
        Arrays.sort(small);
        answer = big[big.length - 1] * small[small.length - 1];
        return answer;
    }
}