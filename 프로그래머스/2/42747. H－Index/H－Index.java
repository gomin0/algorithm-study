import java.util.*;

class Solution {
    public int solution(int[] citations) {
        int len = citations.length;
        Arrays.sort(citations);
        for (int i = 0; i < len; i++) {
            if (citations[len-1-i] <= i)
                return i;
        }
        return len;
    }
}