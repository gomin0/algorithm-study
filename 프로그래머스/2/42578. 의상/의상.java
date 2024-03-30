import java.util.*;
class Solution {
    public int solution(String[][] clothes) {
        Map<String, Integer> map = new HashMap<>();
        int answer = 1;
        for (int i = 0; i < clothes.length; i++) {
            int count = 1;
            if (map.get(clothes[i][1]) == null) {
                map.put(clothes[i][1], 1);
            }
            else {
                map.put(clothes[i][1], map.get(clothes[i][1]) + 1);
            }
        }
        
        for(String s : map.keySet()) {
			answer *= (map.get(s) + 1);
		}
        
        return answer - 1;
    }
}