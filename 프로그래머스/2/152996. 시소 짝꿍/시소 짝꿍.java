import java.util.*;

class Solution {
    public long solution(int[] weights) {
        Arrays.sort(weights);
        Map<Integer, Long> countMap = new HashMap<>();
        long answer = 0;

        for (int w : weights) {
            answer += countMap.getOrDefault(w, 0L);
            if (w * 2 % 3 == 0)
                answer += countMap.getOrDefault(w * 2 / 3, 0L);
            if (w % 2 == 0)
                answer += countMap.getOrDefault(w / 2, 0L);
            if (w * 3 % 4 == 0)
                answer += countMap.getOrDefault(w * 3 / 4, 0L);

            countMap.put(w, countMap.getOrDefault(w, 0L) + 1);
        }

        return answer;
    }
}
