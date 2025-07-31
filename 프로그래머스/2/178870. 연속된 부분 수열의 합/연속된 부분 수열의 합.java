import java.util.*;

class Solution {
    public int[] solution(int[] sequence, int k) {
        int[] answer = {};
        List<int[]> idx = new ArrayList<>();
        int left = 0;
        int right = 0;
        int sum = sequence[0];
        while (right < sequence.length) {
            if (sum == k) {
                idx.add(new int[]{left, right});
                sum -= sequence[left++];
            }
            else if (sum < k) {
                right++;
                if (right < sequence.length)
                    sum += sequence[right];
            }
            else {
                sum -= sequence[left++];
            }
        }
        
        int max = Integer.MAX_VALUE;
        for (int[] i : idx) {
            int l = i[0];
            int r = i[1];
            int diff = r - l;
            if (diff < max) {
                answer = i;
                max = diff;
            }
        }
        
        return answer;
    }
}