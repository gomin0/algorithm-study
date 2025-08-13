import java.util.*;

class Solution {
    Map<String, Integer> map = new HashMap<>();

    public String[] solution(String[] orders, int[] course) {
        List<String> answer = new ArrayList<>();

        for (int len : course) {
            map.clear();
            for (String order : orders) {
                char[] arr = order.toCharArray();
                Arrays.sort(arr);
                combination(arr, new StringBuilder(), 0, len);
            }

            int max = 0;
            for (int v : map.values()) {
                max = Math.max(max, v);
            }

            if (max >= 2) {
                for (String key : map.keySet()) {
                    if (map.get(key) == max) {
                        answer.add(key);
                    }
                }
            }
        }

        Collections.sort(answer);
        return answer.toArray(new String[0]);
    }

    private void combination(char[] arr, StringBuilder sb, int idx, int targetLen) {
        if (sb.length() == targetLen) {
            map.put(sb.toString(), map.getOrDefault(sb.toString(), 0) + 1);
            return;
        }
        for (int i = idx; i < arr.length; i++) {
            sb.append(arr[i]);
            combination(arr, sb, i + 1, targetLen);
            sb.deleteCharAt(sb.length() - 1);
        }
    }
}
