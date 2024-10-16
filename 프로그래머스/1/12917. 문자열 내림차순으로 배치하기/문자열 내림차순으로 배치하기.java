import java.util.*;

class Solution {
    public String solution(String s) {
        char[] charArray = s.toCharArray();
        Arrays.sort(charArray);
        
        String sortedString = new StringBuilder(new String(charArray)).reverse().toString();
        return sortedString;
    }
}