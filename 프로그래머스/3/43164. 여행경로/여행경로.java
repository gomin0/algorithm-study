import java.util.*;

class Solution {
    public String[] solution(String[][] tickets) {
        Map<String, List<String>> map = new HashMap<>();
        for (String[] ticket : tickets) {
            String from = ticket[0];
            String to = ticket[1];
            if (!map.containsKey(from)) map.put(from, new ArrayList<>());
            map.get(from).add(to);
        }
        for (String key : map.keySet()) Collections.sort(map.get(key));

        List<String> route = new ArrayList<>();
        Stack<String> stack = new Stack<>();
        stack.push("ICN");
        
        while (!stack.isEmpty()) {
            String city = stack.peek();
            if (map.containsKey(city) && !map.get(city).isEmpty()) {
                String next = map.get(city).remove(0);
                stack.push(next);
            } else {
                route.add(0, stack.pop());
            }
        }
        
        return route.toArray(new String[route.size()]);
    }
}