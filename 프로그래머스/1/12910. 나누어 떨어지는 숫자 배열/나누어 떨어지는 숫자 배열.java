import java.util.*;

class Solution {
    public List<Integer> solution(int[] arr, int divisor) {
        List<Integer> answer = new ArrayList<>();
        
        Arrays.sort(arr);
        
        for (int i = 0; i < arr.length; i++) {
            int num = arr[i];
            if (num % divisor == 0) {
                answer.add(num);
            }
        }
        
        if (answer.size() == 0) {
            answer.add(-1);
        }
        
        return answer;
    }
}