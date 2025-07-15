import java.util.*;

class Solution {
    public int solution(int[] order) {
        Queue<Integer> belt = new ArrayDeque<>();
        Stack<Integer> container = new Stack<>();
        for (int i = 1; i <= order.length; i++)
            belt.offer(i);
        
        int answer = 0;
        int idx = 0;
        while (!belt.isEmpty() || !container.isEmpty()) {
            int box = order[idx];
            int beltBox = !belt.isEmpty() ? belt.peek() : 0;
            int conBox = !container.isEmpty() ? container.peek() : 0;
            if (box == beltBox)
                belt.poll();
            else if (box == conBox)
                container.pop();
            else {
                if (belt.isEmpty())
                    break;
                else {
                container.push(belt.poll());
                continue;
                }
            }
            answer++;
            idx++;
        }
        
        return answer;
    }
}