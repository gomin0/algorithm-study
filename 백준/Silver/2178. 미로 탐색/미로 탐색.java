import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
    static int n, m;
    static int[][] map;
    static boolean[][] visited;

    // 이동할 네 가지 방향 정의 (상, 하, 좌, 우) 
    static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0, 0, -1, 1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // 입력값 받기 
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        // 미로 정보 초기화 
        map = new int[n][m];
        visited = new boolean[n][m];

        for (int i = 0; i < n; i++) {
            String line = br.readLine();
            for (int j = 0; j < m; j++) {
                map[i][j] = line.charAt(j) - '0';
            }
        }

        // BFS 탐색 수행 
        bfs(0, 0);

        // 결과 출력 
        System.out.println(map[n - 1][m - 1]);
    }

    static void bfs(int x, int y) {
        Queue<int[]> q = new LinkedList<>();
        q.offer(new int[]{x, y});

        visited[x][y] = true;

        while (!q.isEmpty()) {
            int[] current = q.poll();
            int cx = current[0];
            int cy = current[1];

            for (int i = 0; i < 4; i++) {
                int nx = cx + dx[i];
                int ny = cy + dy[i];

                // 미로 범위를 벗어나면 skip 
                if (nx < 0 || ny < 0 || nx >= n || ny >= m) continue;

                // 벽이면 skip 
                if (map[nx][ny] == 0) continue;

                // 이미 방문한 경우 skip 
                if (visited[nx][ny]) continue;

                // 최단 거리를 갱신하고 큐에 넣음 
                map[nx][ny] = map[cx][cy] + 1;
                visited[nx][ny] = true;
                q.offer(new int[]{nx, ny});
            }
        }
    }
}