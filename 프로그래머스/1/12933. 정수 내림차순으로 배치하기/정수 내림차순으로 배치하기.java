import java.util.*;

class Solution {
    public long solution(long n) {
        
        // 1. 정수를 문자열로 변환
        String str = Long.toString(n);
        
        // 2. 문자열을 문자 배열로 변환
        char[] c = str.toCharArray();
        
        // 3. 문자 배열을 오름차순으로 정렬
        Arrays.sort(c);
        
        // 4. 정렬된 배열을 StringBuilder로 변환하고 역순으로 뒤집기
        StringBuilder sortedStr = new StringBuilder(new String(c)).reverse();
        
        // 5. StringBuilder를 문자열로 변환하고 정수로 파싱
        long answer = Long.parseLong(sortedStr.toString());
        
        return answer;
    }
}