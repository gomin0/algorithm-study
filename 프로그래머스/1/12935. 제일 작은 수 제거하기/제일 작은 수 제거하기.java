import java.util.*;

class Solution {
    public int[] solution(int[] arr) {
        
        int len = arr.length;
        
        int[] answer = new int[len - 1];
        if (arr.length == 1) {
            return new int[]{-1};
        }
        
        int min_value = arr[0];
        for (int i = 1; i < len; i++) {
            if (min_value > arr[i]) {
                min_value = arr[i];
            }
        }
        
        ArrayList<Integer> list = new ArrayList<>();
        for (int num : arr) {
            if (num != min_value) {
                list.add(num);
            }
        }
        
        for (int i = 0; i < len-1; i++) {
            answer[i] = list.get(i);
        }
         
        return answer;
    }
}