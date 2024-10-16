import java.util.*;

class Solution {
    public List<Long> solution(int x, int n) {
        List<Long> answer = new ArrayList<>();
        
        for (int i = 0; i < n; i++) {
            answer.add((long) x*(i+1));
        }
        
        return answer;
    }
}