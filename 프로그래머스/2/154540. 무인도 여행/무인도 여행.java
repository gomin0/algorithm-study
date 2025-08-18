import java.util.*;

class Solution {
    int n, m;
    boolean[][] visited;
    int[] dx = {-1, 1, 0, 0};
    int[] dy = {0, 0, 1, -1};
    
    public int[] solution(String[] maps) {
        n = maps.length;
        m = maps[0].length();
        visited = new boolean[n][m];
        List<Integer> answer = new ArrayList<>();
        
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (!visited[i][j] && maps[i].charAt(j) != 'X') {
                    answer.add(bfs(i, j, maps));
                }
            }
        }
        
        if (answer.isEmpty()) return new int[]{-1};
        Collections.sort(answer);
        return answer.stream().mapToInt(Integer::intValue).toArray();
    }
    
    private int bfs(int sx, int sy, String[] maps) {
        Queue<int[]> q = new LinkedList<>();
        q.add(new int[]{sx, sy});
        visited[sx][sy] = true;
        int sum = maps[sx].charAt(sy) - '0';
        
        while (!q.isEmpty()) {
            int[] now = q.poll();
            int x = now[0], y = now[1];
            for (int d = 0; d < 4; d++) {
                int nx = x + dx[d];
                int ny = y + dy[d];
                if (0 <= nx && nx < n && 0 <= ny && ny < m) {
                    if (!visited[nx][ny] && maps[nx].charAt(ny) != 'X') {
                        visited[nx][ny] = true;
                        sum += maps[nx].charAt(ny) - '0';
                        q.add(new int[]{nx, ny});
                    }
                }
            }
        }
        return sum;
    }
}