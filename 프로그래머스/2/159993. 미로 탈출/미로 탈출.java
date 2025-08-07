import java.util.*;

class Solution {
    public int solution(String[] maps) {
        int n = maps.length;
        int m = maps[0].length();
        int startX = 0, startY = 0, leverX = 0, leverY = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                char c = maps[i].charAt(j);
                if (c == 'S') {
                    startX = i;
                    startY = j;
                }
                if (c == 'L') {
                    leverX = i;
                    leverY = j;
                }
            }
        }
        
        int dist1 = bfs(maps, startX, startY, 'L');
        int dist2 = bfs(maps, leverX, leverY, 'E');
        
        if (dist1 == -1 || dist2 == -1)
            return -1;
        else
            return dist1 + dist2;
    }
    
    private int bfs(String[] maps, int startX, int startY, char target) {
        int n = maps.length;
        int m = maps[0].length();
        int[][] distance = new int[n][m];
        boolean[][] visited = new boolean[n][m];
        int[] dx = {-1, 1, 0, 0};
        int[] dy = {0, 0, -1, 1};

        Queue<int[]> q = new LinkedList<>();
        q.add(new int[]{startX, startY});
        visited[startX][startY] = true;
        distance[startX][startY] = 0;

        while (!q.isEmpty()) {
            int[] curr = q.poll();
            int x = curr[0];
            int y = curr[1];

            if (maps[x].charAt(y) == target) {
                return distance[x][y];
            }

            for (int i = 0; i < 4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];

                if (nx >= 0 && ny >= 0 && nx < n && ny < m) {
                    if (!visited[nx][ny] && maps[nx].charAt(ny) != 'X') {
                        visited[nx][ny] = true;
                        distance[nx][ny] = distance[x][y] + 1;
                        q.add(new int[]{nx, ny});
                    }
                }
            }
        }

        return -1;
    }
}