import java.util.*;

class Solution {
    public int[] solution(int n, int m) {
        
        int gcdValue = gcd(n, m);
        int lcmValue = n * m / gcdValue;
        
        return new int[] {gcdValue, lcmValue};
    }
    
    private int gcd(int a, int b) {
        while (b != 0) {
            int temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    }
}