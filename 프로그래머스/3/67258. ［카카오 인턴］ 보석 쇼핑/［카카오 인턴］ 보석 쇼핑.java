import java.util.*;

class Solution {
    public int[] solution(String[] gems) {
        Set<String> gemType = new HashSet<>(Arrays.asList(gems));
        int total = gemType.size();
        Map<String, Integer> counter = new HashMap<>();
        int l = 0, r = 0;
        int minLen = gems.length;
        int answerL = 0, answerR = gems.length-1;
        while (r < gems.length) {
            String gem = gems[r];
            counter.put(gem, counter.getOrDefault(gem, 0) + 1);
            while (counter.size() == total && l <= r) {
                if (r - l < minLen) {
                    minLen = r - l;
                    answerL = l;
                    answerR = r;
                }
                String lGem = gems[l];
                counter.put(lGem, counter.get(lGem) - 1);
                if (counter.get(lGem) == 0) counter.remove(lGem);
                l++;
            }
            r++;
        }
        
        return new int[]{answerL+1, answerR+1};
    }
}