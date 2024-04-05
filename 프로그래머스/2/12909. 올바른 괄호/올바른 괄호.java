import java.util.*;
class Solution {
    boolean solution(String s) {
//         boolean answer = true;
//         Queue<String> q = new LinkedList<>();

//         for (String str : s.split("")) {
//             q.add(str);
//         }
        
//         int count = 0;
        
//         while(!q.isEmpty()) {
//             if (count < 0) {
//                 answer =  false;
//                 break;
//             }
//             if(q.poll().equals("(")) {
//                 count++;
//             }
//             else {
//                 count--;
//             }
//         }
//         if (count != 0) {
//             answer = false;
//         }
//         return answer;
        
        Queue<Character> queue = new LinkedList<>();

        for (char c : s.toCharArray()) {
            if (c == '(') {
                queue.add(c);
            } else if (c == ')') {
                if (queue.isEmpty() || queue.poll() != '(') {
                    return false;
                }
            }
        }

        return queue.isEmpty();
    }
}