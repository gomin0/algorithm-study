class Solution {
    public int solution(String t, String p) {
        int answer = 0;
        long pValue = Long.parseLong(p);
        
        int n = p.length();
        
        for (int i = 0; i <= t.length() - n; i++) {
            String subString = t.substring(i, i + n);
            long subValue = Long.parseLong(subString);
            
            if (subValue <= pValue) {
                answer++;
            }
        }
        
        return answer;
    }
}