class Solution {
    public long solution(int n) {
        long answer = 0;
        if (n == 1) {
            return 1;
        }
        if (n == 2) {
            return 2;
        }
        
        int[] jump = new int[n+1];
        jump[1] = 1;
        jump[2] = 2;
        
        for (int i = 3; i <= n; i++) {
            jump[i] = (jump[i-1] + jump[i-2]) % 1234567;
        }
        
        return jump[n];
    }
}