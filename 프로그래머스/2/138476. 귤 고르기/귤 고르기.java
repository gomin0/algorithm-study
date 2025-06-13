import java.util.*;

class Solution {
    public int solution(int k, int[] tangerine) {
        int answer = 0;
        Map<Integer, Integer> count = new HashMap<>();
        
        for (int size : tangerine) {
            count.put(
                size,
                count.getOrDefault(size, 0) + 1
            );
        }
        
        List<Integer> counts = new ArrayList<>(count.values());
        counts.sort(Collections.reverseOrder());
        for (int c : counts) {
            k -= c;
            answer++;
            if (k <= 0) {
                break;
            }
        }
        
        return answer;
    }
}