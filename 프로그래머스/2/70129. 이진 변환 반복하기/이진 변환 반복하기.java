import java.util.*;

class Solution {
    public int[] solution(String s) {
        int[] answer = new int[2];
        int count = 0;
        int zero = 0;
        
        while (!s.equals("1")) {
            Queue<String> q = new LinkedList<>();
            count ++;
            for (String str : s.split("")) {
                if(str.equals("0")) {
                    zero++;
                }
                else {
                    q.add(str);   
                }
            }
            s = Integer.toBinaryString(q.size());
        }
        
        answer[0] = count;
        answer[1] = zero;
        
        return answer;
    }
}