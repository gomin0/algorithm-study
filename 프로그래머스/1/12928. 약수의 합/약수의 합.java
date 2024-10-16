class Solution {
    public int solution(int n) {
        int answer = 0;
        int num = (int) Math.sqrt(n);
        
        for (int i = 1; i <= num; i++) {
            if (n % i == 0) {
                answer += i;
                if (i != n/i){
                    answer += n / i;
                }
            }
        }
        
        return answer;
    }
}