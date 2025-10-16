import java.util.*;

class Solution {
    static List<List<Node>> graph;
    static int INF = Integer.MAX_VALUE;
    
    class Node implements Comparable<Node> {
        int n;
        int w;
        
        Node(int n, int w) {
            this.n = n;
            this.w = w;
        }
        
        @Override
        public int compareTo(Node node) {
            return this.w - node.w;
        }
    }
    
    public int solution(int n, int s, int a, int b, int[][] fares) {
        graph = new ArrayList<>();
        for (int i = 0; i <= n; i++)
            graph.add(new ArrayList<>());
        
        for (int[] fare : fares) {
            int n1 = fare[0], n2 = fare[1], w = fare[2];
            graph.get(n1).add(new Node(n2, w));
            graph.get(n2).add(new Node(n1, w));
        }
        
        int[] dist1 = dijkstra(s, n);
        int[] dist2 = dijkstra(a, n);
        int[] dist3 = dijkstra(b, n);
        
        int answer = INF;
        for (int i = 1; i <= n; i++) {
            answer = Math.min(answer, dist1[i] + dist2[i] + dist3[i]);
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
                int cost = node.w + nextNode.w;
                if (dist[nextNode.n] > cost) {
                    dist[nextNode.n] = cost;
                    pq.offer(new Node(nextNode.n, cost));
                }
            }
        }
        return dist;
    }
}