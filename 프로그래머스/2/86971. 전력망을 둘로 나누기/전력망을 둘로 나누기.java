import java.util.*;

class Solution {
    public int solution(int n, int[][] wires) {
        int answer = n;
        int[][] graph = new int[n+1][n+1];
        
        // 그래프 생성
        for (int i = 0; i < wires.length; i++) {
            int a = wires[i][0];
            int b = wires[i][1];
            graph[a][b] = 1;
            graph[b][a] = 1;
        }
        
        for (int i = 0; i < wires.length; i++) {
            int a = wires[i][0];
            int b = wires[i][1];
            graph[a][b] = 0;  // 빼기
            graph[b][a] = 0;  // 빼기
            int group = bfs(n, a, graph);  // 두 그룹 전선 수 차이
            
            answer = Math.min(answer, group);
            
            graph[a][b] = 1;  // 복구
            graph[b][a] = 1;  // 복구
        }
        
        return answer;
    }
    
    // 연결 전력망 탐색
    private static int bfs(int n, int start, int[][] graph) {
        boolean[] visited = new boolean[n+1];
        int count = 1;
        
        Queue<Integer> queue = new LinkedList<>();
        visited[start] = true;
        queue.offer(start);
        
        while (!queue.isEmpty()) {
            int node = queue.poll();
            
            for (int i = 1; i <= n; i++) {
                if (graph[node][i] == 1 && !visited[i]) {
                    visited[i] = true;
                    queue.offer(i);
                    count++;
                }
            }
        }
        return Math.abs(count - (n - count));  // 차이 값
    }
}