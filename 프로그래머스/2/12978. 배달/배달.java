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
    
    public int solution(int N, int[][] road, int K) {
        graph = new ArrayList<>();
        for (int i = 0; i <= N; i++) {
            graph.add(new ArrayList<>());
        }
        
        for (int[] r : road) {
            int a = r[0], b = r[1], w = r[2];
            graph.get(a).add(new Node(b, w));
            graph.get(b).add(new Node(a, w));
        }
        
        int[] dist = dijkstra(1, N);
        int answer = 0;
        for (int i = 0; i <= N; i++) {
            if (dist[i] <= K) answer++;
        }

        return answer;
    }
    
    private int[] dijkstra(int start, int n) {
        int[] dist = new int[n + 1];
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