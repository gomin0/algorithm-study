class Solution {
    public String solution(int n, int t, int m, int p) {
        StringBuilder answer = new StringBuilder();
        StringBuilder gameSequence = new StringBuilder();
        
        int num = 0;
        while (gameSequence.length() < t * m) {
            gameSequence.append(convertToBase(num, n));
            num++;
        }
        
        for (int i = 0; i < t; i++) {
            int idx = (p-1) + i*m;
            answer.append(gameSequence.charAt(idx));
        }
        return answer.toString();
    }
    
    private String convertToBase(int num, int base) {
        if (num == 0)
            return "0";
        
        StringBuilder sb = new StringBuilder();
        while (num > 0) {
            int remain = num % base;
            if (remain < 10)
                sb.append(remain);
            else
                sb.append((char) ('A' + remain - 10));
            num /= base;
        }
        return sb.reverse().toString();
    }
}