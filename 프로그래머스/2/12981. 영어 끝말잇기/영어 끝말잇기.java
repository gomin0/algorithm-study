import java.util.*;

class Solution {
    public int[] solution(int n, String[] words) {
        int[] answer = new int[2];
        Set<String> usedWords = new HashSet<>();
        String prevWord = words[0];
        usedWords.add(prevWord);
        
        boolean success = true;
        int i;
        for (i = 1; i < words.length; i++) {
            String word = words[i];
            if (
                usedWords.contains(word) || word.charAt(0) != prevWord.charAt(prevWord.length() - 1)
            ) {
                success = false;
                break;
            }
            usedWords.add(word);
            prevWord = word;
        }
        
        if (success) {
            return answer;
        }
        answer[0] = (i % n) + 1;
        answer[1] = i / n + 1;
        return answer;
    }
}