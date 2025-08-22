import java.util.*;

class Solution {
    static boolean[] visited;
    public int solution(int n, int[][] computers) {
        Map<Integer, List<Integer>> graph = new HashMap<>();
        for (int i = 0; i < n; i++) graph.put(i, new ArrayList<>());
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (i != j && computers[i][j] == 1)
                    graph.get(i).add(j);
            }
        }
        
        visited = new boolean[n];
        int answer = 0;
        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                // bfs(n, computers, i, graph);
                dfs(n, computers, i, graph);
                answer++;
            }
        }
        return answer;
    }
    
    private void bfs(int n, int[][] computers, int start, Map<Integer, List<Integer>> graph) {
        Queue<Integer> q = new LinkedList<>();
        q.add(start);
        visited[start] = true;
        while (!q.isEmpty()) {
            int node = q.poll();
            for (int nextNode : graph.get(node)) {
                if (!visited[nextNode]) {
                    q.add(nextNode);
                    visited[nextNode] = true;
                }
            }
        }
    }
    
    private void dfs(int n, int[][] computers, int start,  Map<Integer, List<Integer>> graph) {
        Stack<Integer> s = new Stack<>();
        s.push(start);
        visited[start] = true;
        while (!s.isEmpty()) {
            int node = s.pop();
            for (int nextNode : graph.get(node)) {
                if (!visited[nextNode]) {
                    s.push(nextNode);
                    visited[nextNode] = true;
                }
            }
        }
    }
}