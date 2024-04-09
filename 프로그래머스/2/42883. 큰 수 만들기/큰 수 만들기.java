import java.util.*;
class Solution {
    public String solution(String number, int k) {
        String answer = "";
        
        char[] arr = number.toCharArray();
        
        StringBuilder sb = new StringBuilder();
        
        int idx = 0;
        
        for (int i = 0; i < arr.length - k; i++) {
            char max = '0';
            for (int j = idx; j <= i + k; j++) {
                if (arr[j] > max) {
                    max = arr[j];
                    idx = j + 1;
                }
            }
            sb.append(Character.toString(max));
        }
         answer = sb.toString();
        return answer;
    }
}