import java.util.*;
class Solution {
    public int solution(int[] priorities, int location) {
        int answer = 0;
        Queue<Integer> q = new LinkedList<>();
        for (int process : priorities) {
            q.add(process);
        }
        
        while(!q.isEmpty()) {
            int a = q.poll();
            boolean big = true;
            for (int i : q) {
                if (i > a) {
                    big = false;
                    break;
                }
            }
            if (big == true) {
                answer++;
                if (location == 0) {
                    return answer;
                }
            } else {
                q.add(a);
            }
            
            if (location == 0) {
                location = q.size() - 1;
            } else {
                location--;
            }
        }
        return answer;
    }
}

// import java.util.*;
// class Solution {
//     public int solution(int[] priorities, int location) {
//         Queue<Integer> q = new LinkedList<>();
//         int answer = 0;
//         // int find = priorities[location];
//         for (int proccess : priorities) {
//             q.add(proccess);
//         }
        
//         while(!q.isEmpty()) {
//             int a = q.poll();
//             boolean check = false;
//             for(int i : q) {
//                 if(i > a) {
//                     check = true;
//                     break;
//                 }
//             }
//             if (check) {
//                 q.add(a);
//             }
//             else{
//                 answer++;
//                 // if(a == find) {
//                 // break;
//                 // } 
//                 if (location == 0) {
//                     break;
//                 }
//             }
//             location --;
//             if (location < 0) {
//                 location = q.size() - 1;
//             }
//         }
        
//         return answer;
//     }
// }