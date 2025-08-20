import java.util.*;

class Solution {
    public int solution(int n, int k, int[] enemy) {
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        int len = enemy.length;
        int e = 0;        
        for (int i = 0; i < len; i++) {
            int amount = enemy[i];
            e += amount;
            pq.add(-amount);
            if (e > n) {
                if (k > 0) {
                    k--;
                    e += pq.poll();
                }
                else {
                    return i;
                }
            }
            
        }
        
        return len;
    }
}