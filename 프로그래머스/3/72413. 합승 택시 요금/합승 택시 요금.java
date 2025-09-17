import java.util.*;

class Solution {
    static List<List<Node>> graph;
    static final int INF = Integer.MAX_VALUE;
    
    class Node implements Comparable<Node> {
        int node;
        int weight;

        Node(int node, int weight) {
            this.node = node;
            this.weight = weight;
        }

        @Override
        public int compareTo(Node other) {
            return this.weight - other.weight;  // minheap
        }
    }
    
    public int solution(int n, int s, int a, int b, int[][] fares) {
        graph = new ArrayList<>();
        for (int i = 0; i <= n; i++) graph.add(new ArrayList<>());
        for (int[] fare : fares) {
            int u = fare[0], v = fare[1], w = fare[2];
            graph.get(u).add(new Node(v, w));
            graph.get(v).add(new Node(u, w));
        }
        
        int[] distS = dijkstra(s, n);
        int[] distA = dijkstra(a, n);
        int[] distB = dijkstra(b, n);
        
        int answer = INF;
        for (int k = 1; k <= n; k++)
            answer = Math.min(answer, distS[k] + distA[k] + distB[k]);
        
        return answer;
    }
    
    private int[] dijkstra(int start, int n) {
        int[] dist = new int[n+1];
        Arrays.fill(dist, INF);
        dist[start] = 0;
        PriorityQueue<Node> pq = new PriorityQueue<>();
        pq.offer(new Node(start, 0));
        
        while (!pq.isEmpty()) {
            Node node = pq.poll();
            int u = node.node;
            int w = node.weight;
            if (w > dist[u]) continue;
            for (Node next : graph.get(u)) {
                int v = next.node;
                int nw = next.weight + w;
                if (nw < dist[v]) {
                    dist[v] = nw;
                    pq.offer(new Node(v, nw));
                }
            }
        }
        return dist;
    }
}