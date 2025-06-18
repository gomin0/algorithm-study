import java.util.*;

class Solution {
    public int solution(String[][] clothes) {
        int answer = 1;
        Map<String, Integer> clothesCounts = new HashMap<>();
        
        for (String[] items : clothes) {
            String clothesType = items[1];
            clothesCounts.put(
                clothesType,
                clothesCounts.getOrDefault(clothesType, 0) + 1
            );
        }
        
        for (int count : clothesCounts.values()) {
            answer *= count + 1;
        }
        
        answer--;
        return answer;
    }
}