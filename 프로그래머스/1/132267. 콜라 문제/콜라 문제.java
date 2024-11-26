class Solution {
    public int solution(int a, int b, int n) {
        int answer = 0;
        
        while (n >= a) {
            int bottle = (n / a) * b;
            int rest = n % a;  // 나머지
            answer += bottle;
            n = rest + bottle;
        }
        
        return answer;
    }
}