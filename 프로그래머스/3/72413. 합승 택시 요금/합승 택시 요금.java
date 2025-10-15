import java.util.*;

class Solution {
    static List<List<Node>> graph;
    static final int INF = Integer.MAX_VALUE;
    
    class Node implements Comparable<Node> {
        int n;
        int w;
        
        Node(int n, int w) {
            this.n = n;
            this.w = w;
        }
        
        @Override
        public int compareTo(Node n2) {
            return this.w - n2.w;
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
        
        int[] dist1 = dijkstra(s, n);
        int[] dist2 = dijkstra(a, n);
        int[] dist3 = dijkstra(b, n);
        
        int answer = INF;
        for (int k = 1; k <= n; k++) {
            answer = Math.min(answer, dist1[k] + dist2[k] + dist3[k]);
        }
        
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
            if (node.w > dist[node.n]) continue;
            for (Node nextNode : graph.get(node.n)) {
                int w = nextNode.w + node.w;
                if (w < dist[nextNode.n]) {
                    dist[nextNode.n] = w;
                    pq.offer(new Node(nextNode.n, w));
                }
            }
        }
        return dist;
    }
}