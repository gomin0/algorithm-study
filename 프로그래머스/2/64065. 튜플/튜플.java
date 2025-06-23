import java.util.*;

class Solution {
    public List<Integer> solution(String s) {
        List<Integer> answer = new ArrayList<>();
        Set<Integer> set = new HashSet<>();
        String subS = s.substring(2, s.length() - 2);
        String[] subTuple = subS.split("\\},\\{");
        Arrays.sort(subTuple, (a, b) -> a.length() - b.length());
        for (int i = 0; i < subTuple.length; i++) {
            String[] numbers = subTuple[i].split(",");
            for (String number : numbers) {
                int num = Integer.parseInt(number);
                if (!set.contains(num)) {
                    set.add(num);
                    answer.add(num);
                }
            }
        }
            
        
        return answer;
    }
}