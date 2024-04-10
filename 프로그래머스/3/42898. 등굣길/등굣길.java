class Solution {
    public int solution(int m, int n, int[][] puddles) {
        int mod = 1000000007;
        int[][] dp = new int[m][n];
        for (int[] puddle : puddles) {
            dp[puddle[0] - 1][puddle[1] - 1] = -1;
        }
        
        dp[0][0] = 1;
        
        for(int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if(dp[i][j] == -1) {
                    dp[i][j] = 0;
                    continue;
                }
                
                if(i != 0) // 맨위 아님
                    dp[i][j] += dp[i - 1][j] % mod;

                if(j != 0) // 맨옆 아님
                    dp[i][j] += dp[i][j - 1] % mod;
            }
        }
        return dp[m - 1][n - 1] % mod;
    }
}