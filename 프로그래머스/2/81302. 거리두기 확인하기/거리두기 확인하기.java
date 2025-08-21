import java.util.*;

class Solution {
    private static int[] dx = {-1, 1, 0, 0};
    private static int[] dy = {0, 0, -1, 1};
    
    public int[] solution(String[][] places) {
        int[] answer = new int[5];
        for (int r = 0; r < 5; r++) {
            char[][] room = new char[5][5];
            for (int i = 0; i < 5; i++) {
                room[i] = places[r][i].toCharArray();
            }
            if (isValidRoom(room)) answer[r] = 1;
            else answer[r] = 0;
        }
        return answer;
    }
    
    private boolean isValidRoom(char[][] room) {
        for (int i = 0; i < 5; i++) {
            for (int j = 0; j < 5; j++) {
                if (room[i][j] == 'P') {
                    if (!bfs(room, i, j)) return false;
                }
            }
        }
        return true;
    }
    
    private boolean bfs(char[][] room, int x, int y) {
        Queue<int[]> q = new LinkedList<>();
        boolean[][] visited = new boolean[5][5];
        q.add(new int[]{x, y, 0});
        visited[x][y] = true;
        
        while (!q.isEmpty()) {
            int[] current = q.poll();
            int cx = current[0], cy = current[1], dist = current[2];
            
            if (dist >= 2) continue;
            for (int i = 0; i < 4; i++) {
                int nx = cx + dx[i];
                int ny = cy + dy[i];
                if (nx < 0 || ny < 0 || nx >= 5 || ny >= 5 || visited[nx][ny] || room[nx][ny] == 'X') continue;
                if (room[nx][ny] == 'P') return false;
                q.add(new int[]{nx, ny, dist+1});
                visited[nx][ny] = true;
            }
                
        }
        return true;
    }
}