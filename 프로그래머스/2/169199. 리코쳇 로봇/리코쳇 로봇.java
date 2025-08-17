import java.util.*;

class Solution {
    static class Node{
        int x, y, count;
        Node(int x, int y, int count) {
            this.x = x;
            this.y = y;
            this.count = count;
        }
    }
    
    public int solution(String[] board) {
        int n = board.length;
        int m = board[0].length();
        char[][] map = new char[n][m];
        int sx = 0, sy = 0, gx = 0, gy = 0;
        
        for (int i = 0; i < n; i++) {
            map[i] = board[i].toCharArray();
            for (int j = 0; j < m; j++) {
                if (map[i][j] == 'R') {
                    sx = i;
                    sy = j;
                } else if (map[i][j] == 'G') {
                    gx = i;
                    gy = j;
                }
            }
        }
        
        Queue<Node> q = new LinkedList<>();
        boolean[][] visited = new boolean[n][m];
        q.add(new Node(sx, sy, 0));
        visited[sx][sy] = true;
        int[] dx = {-1, 1, 0, 0};
        int[] dy = {0, 0, -1, 1};
        
        while (!q.isEmpty()) {
            Node current = q.poll();
            if (current.x == gx && current.y == gy) {
                return current.count;
            }
            
            for (int d = 0; d < 4; d++) {
                int x = current.x;
                int y = current.y;
                while(true) {
                    int nx = x + dx[d];
                    int ny = y + dy[d];
                    if (nx < 0 || nx >= n || ny < 0 || ny >= m) break;
                    if (map[nx][ny] == 'D') break;
                    x = nx;
                    y = ny;
                }
                if (!visited[x][y]) {
                    visited[x][y] = true;
                    q.add(new Node(x, y, current.count + 1));
                }
            }
        }
        
        return -1;
    }
}