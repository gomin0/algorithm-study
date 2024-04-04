import java.util.*;
class Solution {
    static int[][] graph;
    
    public int solution(int n, int[][] wires) {
        int answer = n;
        graph = new int[n+1][n+1];
        
        for (int i = 0; i < wires.length; i++) {
            int a = wires[i][0];
            int b = wires[i][1];
            graph[a][b] = 1;
            graph[b][a] = 1;
        }
        
        for(int i=0; i<wires.length; i++){
            int a = wires[i][0];
            int b = wires[i][1];
            graph[a][b] = 0; // 하나 빼기
            graph[b][a] = 0;
            
            answer = Math.min(answer, bfs(n, a));
            graph[a][b] = 1; // 되돌리기
            graph[b][a] = 1;
        }
        
        return answer;
    }
    
    static int bfs(int n, int start) {
        boolean[] visited = new boolean[n + 1];
        int count = 1;
        
        Queue<Integer> q = new LinkedList<>();
        visited[start] = true;
        q.offer(start);
        
        while (!q.isEmpty()) {
            int temp = q.poll();
            
            for(int i = 1; i <= n; i++) {
                if (graph[temp][i] == 1 && !visited[i]) {
                    visited[i] = true;
                    q.offer(i);
                    count++;
                }
            }
        }
        return Math.abs(count - (n - count));
    }
    
}