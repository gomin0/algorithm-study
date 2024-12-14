class Solution {
    public int solution(int n, int m, int[] section) {
        int answer = 0;
        int[] wall = new int[n];
        
        for (int i = 0; i < section.length; i++) {
            wall[section[i] - 1] = 1;
        }
        
        int idx = 0;
        while (idx < n) {
            if (wall[idx] == 1) {
                answer++;
                idx += m;
            }
            else {
                idx++;
            }
        }
        
        return answer;
    }
}