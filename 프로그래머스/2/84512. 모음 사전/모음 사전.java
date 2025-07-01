import java.util.*;

class Solution {
    public int solution(String word) {
        int[] weights = {781, 156, 31, 6, 1};
        Map <Character, Integer> wordDict = new HashMap<>();
        wordDict.put('A', 0);
        wordDict.put('E', 1);
        wordDict.put('I', 2);
        wordDict.put('O', 3);
        wordDict.put('U', 4);
        int answer = 0;
        
        for (int i = 0; i < word.length(); i++) {
            char c = word.charAt(i);
            answer += wordDict.get(c) * weights[i] + 1;
        }
        
        return answer;
    }
}
