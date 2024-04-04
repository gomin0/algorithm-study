import java.util.*;
class Solution {
    public int solution(int[] citations) {
        Arrays.sort(citations);
        
        int n = citations.length;
        for (int i = 0; i < n; i++) {
            int h = n - i;
            if (citations[i] >= h) {
                return h;
            }
        }
        
        return 0;
        
        // for(int i = citations.length - 1; i >= 0; i--) {
        //     int h = citations[i];
        //     int count1 = 0;
        //     int count2 = 0;
        //     for (int j = citations.length - 1; j >= 0; j--) {
        //         if (count1 < h && citations[j] >= h) {
        //             count1++;
        //         }
        //         else if (count1 >= h && citations[j] <= h) {
        //             count2++;
        //         }
        //     }
        //     if(count1 + count2 == citations.length) {
        //         return h;
        //     }
        // }
        
    }
}