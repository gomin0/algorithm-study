import java.util.*;

public class Solution {
    public ArrayList<Integer> solution(int []arr) {
        int[] answer = {};
        ArrayList<Integer> answerList = new ArrayList<>();
        answerList.add(arr[0]);
        
        for(int i = 1; i < arr.length; i++) {
            if(arr[i] != arr[i-1]) {
                answerList.add(arr[i]);
            }
        }

        return answerList;
    }
}

// import java.util.*;

// public class Solution {
//     public int[] solution(int []arr) {
//         List<Integer> answerList = new ArrayList<>();
//         answerList.add(arr[0]);
//         for (int i = 1; i < arr.length; i++) {
//             if (arr[i] != arr[i - 1]) {
//                 answerList.add(arr[i]);
//             }
//         }
//         int[] answer = new int[answerList.size()];
//         for (int i = 0; i < answerList.size(); i++) {
//             answer[i] = answerList.get(i);
//         }
        
//         return answer;
//     }
// }