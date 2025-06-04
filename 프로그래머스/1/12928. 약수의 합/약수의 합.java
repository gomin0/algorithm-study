class Solution {
    public int solution(int n) {
        int answer = 0;
        int num = (int) Math.sqrt(n);
    
        for (int i = 1; i <= num; i++) {
            if (n % i == 0) {
                answer += i;
                int num2 = n / i;
                if (num2 != i) {
                    answer += num2;
                }
            }
        }
        return answer;
    }
}