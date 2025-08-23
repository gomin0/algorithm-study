import java.util.*;

class Solution {
    public int solution(int[] A, int[] B) {
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        for (int num : B) pq.offer(num);
        Arrays.sort(A);
        int idx = 0;
        int n = A.length;
        int answer = 0;
        while (idx < n && !pq.isEmpty()) {
            int aNum = A[idx];
            int bNum = pq.poll();
            if (aNum < bNum) {
                answer++;
                idx++;
            }
        }
        return answer;
    }
}