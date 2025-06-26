import java.util.*;

class Solution {
    public int solution(int[] topping) {
        Map<Integer, Integer> toppingType1 = new HashMap<>();
        Map<Integer, Integer> toppingType2 = new HashMap<>();
        for (int t : topping) {
            toppingType1.put(t, toppingType1.getOrDefault(t, 0) + 1);
        }

        int answer = 0;
        for (int i = 0; i < topping.length; i++) {
            int top = topping[i];
            toppingType1.put(top, toppingType1.get(top) - 1);
            if (toppingType1.get(top) == 0)
                toppingType1.remove(top);
            toppingType2.put(top, toppingType2.getOrDefault(top, 0) + 1);

            if (toppingType1.size() == toppingType2.size())
                answer++;
        }
        
        return answer;
    }
}