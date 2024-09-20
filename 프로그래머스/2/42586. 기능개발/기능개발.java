import java.util.*;

class Solution {
    public ArrayList<Integer> solution(int[] progresses, int[] speeds) {
        ArrayList<Integer> answer = new ArrayList<>();
        int[] done = new int[progresses.length];
        int day = 0;
        int count = 0;
        
        for(int i = 0; i < progresses.length; i++) {
            int nextDay = (100 - progresses[i]) / speeds[i];
            if ((100 - progresses[i]) % speeds[i] != 0) {
                nextDay += 1;
            }
            
            if (day >= nextDay) {
                count += 1;
            } else{
                if (count != 0) {
                    answer.add(count);
                }
                count = 1;
                day = nextDay;
            }
        }
        answer.add(count);
        
        return answer;
    }
}

// import java.util.*;
// class Solution {
//     public int[] solution(int[] progresses, int[] speeds) {
//         ArrayList<Integer> list = new ArrayList<>();
//         int[] finish = new int[progresses.length];
//         for (int i = 0; i < progresses.length; i++) {
//             if ((100 - progresses[i]) % speeds[i] == 0) {
//                 finish[i] = (100 - progresses[i]) / speeds[i];
//             }
//             else {
//                 finish[i] = (100 - progresses[i]) / speeds[i] + 1;
//             }
//         }
        
//         // for (int i = 0; i < finish.length; i++) {
//         //     int count = 0;
//         //     for (int j = i + 1; j < finish.length; j++) {
//         //         count++;
//         //         if (finish[i] < finish[j]) {
//         //             list.add(count);
//         //             break;
//         //         }
//         //     }
//         // }
        
//         int x = finish[0];
//         int count = 1;
//         for(int i = 1; i < finish.length; i++) {
//             if (x >= finish[i]) {
//                 count++;
//             }
//             else {
//                 list.add(count);
//                 count = 1;
//                 x = finish[i];
//             }
//         }
//         list.add(count);
        
//         int[] answer = new int[list.size()];
//         for (int i = 0; i < list.size(); i++) {
//             answer[i] = list.get(i);
//         }
        
//         return answer;
//     }
// }