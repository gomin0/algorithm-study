public class Solution {
    public int solution(int n) {
        int jump = 0;
        while (n != 0) {
            if (n % 2 == 0) {
                n /= 2;
                continue;
            }
            jump += 1;
            n--;
        }
        return jump;
    }
}