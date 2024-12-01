import java.util.*;

class Solution {
    public int[] solution(int k, int[] score) {
        int n = score.length;
        int[] answer = new int[n];
        PriorityQueue<Integer> hall = new PriorityQueue<>();
        
        for (int i = 0; i < n; i++) {
            hall.add(score[i]);
            
            if (i >= k) {
                hall.poll();

            }
            
            answer[i] = hall.peek();
        }
                    
        
        return answer;
    }
}