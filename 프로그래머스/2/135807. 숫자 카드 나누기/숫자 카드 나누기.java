import java.util.*;

class Solution {
    public int solution(int[] arrayA, int[] arrayB) {
        List<Integer> divisorsA = getAllCd(arrayA);
        List<Integer> divisorsB = getAllCd(arrayB);
        
        int answer = Math.max(
            findAnswer(arrayB, divisorsA), 
            findAnswer(arrayA, divisorsB)
        );
        
        return answer;
    }
    
    private List<Integer> getAllCd(int[] array) {
        int value = array[0];
        for (int i = 1; i < array.length; i++) {
            value = gcd(value, array[i]);
        }
        
        List<Integer> divisors = new ArrayList<>();
        for (int i = 1; i * i <= value; i++) {
            if (value % i == 0) {
                divisors.add(i);
                if (value / i != i)
                    divisors.add(value / i);
            }
        }
        Collections.sort(divisors, Collections.reverseOrder());
        return divisors;
    }
    
    private int gcd(int a, int b) {
        while (b != 0) {
            int temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    }
    
    private int findAnswer(int[] array, List<Integer> divisors) {
        int answer = 0;
        for (int divisor : divisors) {
            boolean possible = true;
            for (int num : array) {
                if (num % divisor == 0) {
                    possible = false;
                    break;
                }
            }
            if (possible) {
                answer = divisor;
                break;
            }
        }
        return answer;
    }
}