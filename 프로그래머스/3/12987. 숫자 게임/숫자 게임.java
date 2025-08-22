import java.util.*;

class Solution {
    public int solution(int[] A, int[] B) {
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        for (int num : B) pq.offer(num);
        Arrays.sort(A);
        int i = 0;
        int n = A.length;
        int answer = 0;
        while (i < n && !pq.isEmpty()) {
            int aNum = A[i];
            int bNum = pq.poll();
            if (aNum < bNum) {
                answer++;
                i++;
            }
        }
        return answer;
    }
}