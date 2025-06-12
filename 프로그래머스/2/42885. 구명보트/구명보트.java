import java.util.Arrays;

class Solution {
    public int solution(int[] people, int limit) {
        int answer = 0;
        int len = people.length;
        int i, j;
        i = 0;
        j = len-1;
        Arrays.sort(people);
        
        while (i <= j) {
            int min = people[i];
            int max = people[j];
            if ((min + max) <= limit)
                i++;
            j--;
            answer += 1;
        }
        return answer;
    }
}