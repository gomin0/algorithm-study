import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int[][] graph;
    static boolean[] visited;
    static int n, m;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        n = Integer.parseInt(br.readLine()); // 컴퓨터의 수
        m = Integer.parseInt(br.readLine()); // 연결된 컴퓨터 쌍의 수

        graph = new int[n + 1][n + 1]; // 인접 행렬
        visited = new boolean[n + 1]; // 방문 여부 배열

        // 그래프 구성
        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());

            graph[u][v] = graph[v][u] = 1;
        }

        int answer = dfs(1); // 1번 컴퓨터와 연결된 컴퓨터들을 찾아서 개수를 반환
        System.out.println(answer);
    }

    // 깊이 우선 탐색(DFS)
    static int dfs(int v) {
        visited[v] = true;
        int count = 0;

        for (int i = 1; i <= n; i++) {
            if (graph[v][i] == 1 && !visited[i]) {
                count += dfs(i) + 1;
            }
        }

        return count;
    }
}