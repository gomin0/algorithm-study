import java.util.*;

class Solution {
    static class Word {
        String word;
        int count;
        Word(String word, int count) {
            this.word = word;
            this.count = count;
        }
    }
    static Set<String> wordSet;
    public int solution(String begin, String target, String[] words) {
        wordSet = new HashSet<>();
        int answer = bfs(begin, target, words);
        return answer;
    }
    
    private int bfs(
        String begin,
        String target,
        String[] words
    ) {
        Queue<Word> q = new LinkedList<>();
        q.offer(new Word(begin, 0));
        wordSet.add(begin);
        while (!q.isEmpty()) {
            Word word = q.poll();
            String w = word.word;
            int count = word.count;
            if (w.equals(target)) return count;
            for (String nextWord : words) {
                if (check(w, nextWord) && !wordSet.contains(nextWord)) {
                    q.offer(new Word(nextWord, count+1));
                    wordSet.add(w);
                }
            }
        }
        return 0;
    }
    
    private boolean check(String w1, String w2) {
        int diff = 0;
        for (int i = 0; i < w1.length(); i++) {
            if (w1.charAt(i) != w2.charAt(i)) diff++;
            if (diff > 1) return false;
        }
        if (diff == 1) return true;
        else return false;
    }
}