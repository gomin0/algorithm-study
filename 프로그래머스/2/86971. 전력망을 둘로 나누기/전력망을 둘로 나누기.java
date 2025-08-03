import java.util.*;

class Solution {
    public int solution(int n, int[][] wires) {
        int answer = n;
        int[][] graph = new int[n+1][n+1];
        for (int i = 0; i < wires.length; i++) {
            int a = wires[i][0];
            int b = wires[i][1];
            graph[a][b] = 1;
            graph[b][a] = 1;
        }
        for (int i = 0; i < wires.length; i++) {
            int a = wires[i][0];
            int b = wires[i][1];
            graph[a][b] = 0;
            graph[b][a] = 0;
            answer = Math.min(answer, bfs(n, a, graph));
            graph[a][b] = 1;
            graph[b][a] = 1;
        }
        return answer;
    }
    
    private int bfs(int n, int a, int[][] graph) {
        Queue<Integer> q = new LinkedList<>();
        q.offer(a);
        boolean[] visited = new boolean[n+1];
        visited[a] = true;
        int count = 1;
        while (!q.isEmpty()) {
            int node = q.poll();
            for (int i = 1; i <= n; i++) {
                if(graph[node][i] == 1 && !visited[i]) {
                    visited[i] = true;
                    q.offer(i);
                    count++;
                }
            }
        }
        return Math.abs(count - (n - count));
    }
}