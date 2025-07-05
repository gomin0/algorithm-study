import java.util.*;

class Solution {
    public String solution(String s) {
        StringBuilder sb = new StringBuilder();
        char[] charArray = s.toCharArray();
        Arrays.sort(charArray);
        for(char c : charArray)
            sb.append(c);
        
        return sb.reverse().toString();
    }
}