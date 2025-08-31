import java.util.*;

class Solution {
    private static int[] parent;
    public int solution(int n, int[][] costs) {
        Arrays.sort(costs, (a, b) -> Integer.compare(a[2], b[2]));
        parent = new int[n];
        for (int i = 0; i < n; i++) parent[i] = i;
        
        int answer = 0;
        int count = 0;
        
        for (int[] cost : costs) {
            int a = cost[0], b = cost[1], c = cost[2];
            if (find(a) != find(b)) {
                union(a, b);
                count++;
                answer += c;
            }
            if (count == n-1) break;
        }
        
        return answer;
    }
    
    private int find(int node) {
        if (parent[node] == node) return node;
        return parent[node] = find(parent[node]);
    }
    
    private void union(int a, int b) {
        int pa = find(a);
        int pb = find(b);
        if (pa != pb) parent[pb] = pa;
    }
}