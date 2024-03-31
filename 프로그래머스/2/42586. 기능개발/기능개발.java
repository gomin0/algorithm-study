import java.util.*;
class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        ArrayList<Integer> list = new ArrayList<>();
        int[] finish = new int[progresses.length];
        for (int i = 0; i < progresses.length; i++) {
            if ((100 - progresses[i]) % speeds[i] == 0) {
                finish[i] = (100 - progresses[i]) / speeds[i];
            }
            else {
                finish[i] = (100 - progresses[i]) / speeds[i] + 1;
            }
        }
        
        // for (int i = 0; i < finish.length; i++) {
        //     int count = 0;
        //     for (int j = i + 1; j < finish.length; j++) {
        //         count++;
        //         if (finish[i] < finish[j]) {
        //             list.add(count);
        //             break;
        //         }
        //     }
        // }
        
        int x = finish[0];
        int count = 1;
        for(int i = 1; i < finish.length; i++) {
            if (x >= finish[i]) {
                count++;
            }
            else {
                list.add(count);
                count = 1;
                x = finish[i];
            }
        }
        list.add(count);
        
        int[] answer = new int[list.size()];
        for (int i = 0; i < list.size(); i++) {
            answer[i] = list.get(i);
        }
        
        return answer;
    }
}