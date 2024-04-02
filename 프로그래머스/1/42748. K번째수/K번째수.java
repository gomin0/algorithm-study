import java.util.*;
class Solution {
    public int[] solution(int[] array, int[][] commands) {
        int[] answer = new int[commands.length];
        for (int i = 0; i < commands.length; i++){
            int a = commands[i][0];
            int a2 = a - 1;
            int b = commands[i][1];
            int c = commands[i][2];
            int[] s = new int[b - a + 1];
            for (int j = 0; j < b - a + 1; j++) {
                s[j] = array[a2];
                a2++;
            }
            Arrays.sort(s);
            answer[i] = s[c - 1];
        }
        return answer;
    }
}