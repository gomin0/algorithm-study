import java.util.*;

class Solution {
    public int solution(int[] players, int m, int k) {
        int answer = 0;
        Queue<Integer> server = new ArrayDeque<>();
        
        for (int i = 0; i < players.length; i++) {
            while (!server.isEmpty()) {
                int serverStart = server.peek();
                if ((i - serverStart) >= k)
                    server.poll();
                else
                    break;
            }
            int need = players[i] / m;
            int serverSize = server.size();
            if (need > serverSize) {
                for (int j = 0; j < need-serverSize; j++) {
                    server.add(i);
                    answer++;
                }
            }
        }
        
        return answer;
    }
}