class Solution {
    public int solution(int num) {
        int answer = 0;
        int times = 500;
        long n = num;
        
        while (times > 0) {
            
            if (n == 1) {
                return answer;
            }
            
            if (n % 2 == 0) {
                n /= 2;
            }
            else {
                n = n * 3 + 1;
            }
            times--;
            answer++;
        }
        
        return -1;
    }
}