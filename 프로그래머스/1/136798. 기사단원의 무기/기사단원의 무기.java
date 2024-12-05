class Solution {
    public int countDivisors(int num) {
        int count = 0;
        
        for (int i = 1; i*i <= num; i++) {
            if (num % i == 0) {
                count++;
                if (i != num/i) {
                    count++;
                }
            }
        }
        return count;
    }
    
    
    public int solution(int number, int limit, int power) {
        int answer = 0;
        
        for (int j = 1; j <= number; j++) {
            int divCount = countDivisors(j);
            if (divCount <= limit) {
                answer += divCount;
            }
            else {
                answer += power;
            }
        }
        
        return answer;
    }
}