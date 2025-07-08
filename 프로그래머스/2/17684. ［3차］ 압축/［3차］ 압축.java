import java.util.*;

class Solution {
    public List<Integer> solution(String msg) {
        Map<String, Integer> alphabet = new HashMap<>();
        int alpha = 1;
        for (char c = 'A'; c <= 'Z'; c++) {
            alphabet.put(String.valueOf(c), alpha++);
        }
        
        List<Integer> answer = new ArrayList<>();
        int idx = 0;
        while (idx < msg.length()) {
            String w = "";
            int i = idx;
            while (i < msg.length()) {
                String next_w = msg.substring(idx, i+1);
                if (alphabet.containsKey(next_w)) {
                    w = next_w;
                    i++;
                } else
                    break;
            }
            answer.add(alphabet.get(w));
            if (i < msg.length()) {
                String wc = msg.substring(idx, i+1);
                alphabet.put(wc, alpha++);
            }
            idx += w.length();
        }
        
        return answer;
    }
}