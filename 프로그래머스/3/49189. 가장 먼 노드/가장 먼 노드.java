import java.util.*;

class Solution {
    public int solution(int n, int[][] edge) {
        List<Integer>[] graph = new ArrayList[n+1];
        for (int i = 1; i <= n; i++) graph[i] = new ArrayList<>();
        for(int[] e : edge) {
            int a = e[0], b = e[1];
            graph[a].add(b);
            graph[b].add(a);
        }
        
        int[] dist = new int[n+1];
        Arrays.fill(dist, -1);
        dist[1] = 0;
        
        Queue<Integer> q = new ArrayDeque<>();
        q.offer(1);
        
        while (!q.isEmpty()) {
            int current = q.poll();
            for (int next : graph[current]) {
                if (dist[next] == -1) {
                    dist[next] = dist[current] + 1;
                    q.offer(next);
                }
            }
        }
        
        int max = 0;
        for (int i = 1; i <= n; i++) {
            if (dist[i] > max) max = dist[i];
        }

        int answer = 0;
        for (int i = 1; i <= n; i++) {
            if (dist[i] == max) answer++;
        }
        
        return answer;
    }
}