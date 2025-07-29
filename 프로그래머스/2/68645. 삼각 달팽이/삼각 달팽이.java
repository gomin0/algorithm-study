class Solution {
    public int[] solution(int n) {
        int last = n * n - n * (n - 1) / 2;
        int[][] triangle = new int[n][];
        for (int i = 0; i < n ; i++)
            triangle[i] = new int[i+1];
        int[][] direction = {
            {1, 0},
            {0, 1},
            {-1, -1}
        };
        
        int x = 0;
        int y = 0;
        int dir = 0;
        for (int i = 1; i <= last; i++) {
            triangle[x][y] = i;
            int nx = x + direction[dir][0];
            int ny = y + direction[dir][1];
            if (ny < 0 || ny > x || nx < 0 || nx >= n || triangle[nx][ny] != 0) {
                dir = (dir + 1) % 3;
                nx = x + direction[dir][0];
                ny = y + direction[dir][1];
            }
            x = nx;
            y = ny;
        }
        
        int[] answer = new int[last];
        int idx = 0;
        for (int i = 0; i < n; i++) {
            int[] rowNum = triangle[i];
            for (int num : rowNum) {
                answer[idx++] = num;
            }
        }
        return answer;
    }
}