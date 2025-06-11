class Solution {
    public int solution(int n) {
        int answer = 0;
        
        for (int i = 1; i <= n; i++) {
            int number = 0;
            for (int j = i; j <= n; j++) {
                number += j;
                if (number == n) {
                    answer ++;
                    break;
                }
                else if (number > n)
                    break;
            }
        }
        
        return answer;
    }
}