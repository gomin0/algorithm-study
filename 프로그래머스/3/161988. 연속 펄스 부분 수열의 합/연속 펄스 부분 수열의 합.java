class Solution {
    public long solution(int[] sequence) {
        int n = sequence.length;
        long answer = Long.MIN_VALUE;
        long dp1 = 0;
        long dp2 = 0;
        for (int i = 0; i < n; i++) {
            int val1 = (i % 2 == 0 ? 1 : -1) * sequence[i];
            int val2 = (i % 2 == 0 ? -1 : 1) * sequence[i];
            dp1 = Math.max(val1, dp1 + val1);
            dp2 = Math.max(val2, dp2 + val2);
            answer = Math.max(answer, Math.max(dp1, dp2));
        }
        return answer;
    }
}