import java.util.*;

class Solution {
    public int solution(int cacheSize, String[] cities) {
        List<String> cache = new ArrayList<>();
        int answer = 0;
        
        for (String city : cities) {
            city = city.toLowerCase();
            if (cache.contains(city)) {
                answer++;
                cache.remove(city);
            }
            else {
                answer += 5;
                if (cache.size() == cacheSize && !cache.isEmpty())
                    cache.remove(cache.size() - 1);
            }
            if (cacheSize > 0)
                cache.add(0, city);
        }
        return answer;
    }
}
