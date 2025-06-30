import java.util.*;

class Solution {
    public int solution(String str1, String str2) {
        Map<String, Integer> str1Count = new HashMap<>();
        Map<String, Integer> str2Count = new HashMap<>();
        str1 = str1.toLowerCase();
        str2 = str2.toLowerCase();
        strCount(str1Count, str1);
        strCount(str2Count, str2);
        
        int intersection = 0;
        int union = 0;
        for (String key : str1Count.keySet()) {
            if (str2Count.containsKey(key)) {
                int s1 = str1Count.get(key);
                int s2 = str2Count.get(key);
                if (s1 >= s2) {
                    intersection += s2;
                    union += s1;         
                }
                else {
                    union += s2;
                    intersection += s1; 
                }
                continue;
            }
            union += str1Count.get(key);
        }
        
        for (String key : str2Count.keySet()) {
            if (!str1Count.containsKey(key))
                union += str2Count.get(key);
        }
        
        if (intersection == 0 && union == 0) {
            return 65536;
        }
        
        int answer = (int) (((double) intersection / union) * 65536);
        return answer;
    }
    
    private void strCount(Map<String, Integer> map, String str) {
        for (int i = 0; i < str.length() - 1; i++) {
            String subStr = str.substring(i, i+2);
            if (isValidString(subStr))
                map.put(subStr, map.getOrDefault(subStr, 0) + 1);
        }
    }
    
    private boolean isValidString(String pair) {
        return Character.isLetter(pair.charAt(0)) && 
            Character.isLetter(pair.charAt(1));
    }
}