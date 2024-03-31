import java.util.*;
class Solution {
    public int solution(int[] priorities, int location) {
        Queue<Integer> q = new LinkedList<>();
        int answer = 0;
        // int find = priorities[location];
        for (int proccess : priorities) {
            q.add(proccess);
        }
        
        while(!q.isEmpty()) {
            int a = q.poll();
            boolean check = false;
            for(int i : q) {
                if(i > a) {
                    check = true;
                    break;
                }
            }
            if (check) {
                q.add(a);
            }
            else{
                answer++;
                // if(a == find) {
                // break;
                // } 
                if (location == 0) {
                    break;
                }
            }
            location --;
            if (location < 0) {
                location = q.size() - 1;
            }
        }
        
        return answer;
    }
}