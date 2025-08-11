import java.util.*;

class Solution {
    static class Node implements Comparable<Node> {
        int to, cost;
        Node(int to, int cost) {
            this.to = to;
            this.cost = cost;
        }
        @Override
        public int compareTo(Node o) {
            return this.cost - o.cost;
        }
    }
    
    public int solution(int N, int[][] road, int K) {
        List<List<Node>> graph = new ArrayList<>();
        for (int i = 0; i <= N; i++) {
            graph.add(new ArrayList<>());
        }
        
        for (int[] r : road) {
            int a = r[0], b = r[1], c = r[2];
            graph.get(a).add(new Node(b, c));
            graph.get(b).add(new Node(a, c));
        }
        
        int[] dist = new int[N+1];
        Arrays.fill(dist, Integer.MAX_VALUE);
        dist[1] = 0;
        
        PriorityQueue<Node> pq = new PriorityQueue<>();
        pq.offer(new Node(1, 0));
        
        while (!pq.isEmpty()) {
            Node node = pq.poll();
            if (node.cost > dist[node.to])
                continue;
            for (Node nextNode : graph.get(node.to)) {
                int nextDist = node.cost + nextNode.cost;
                if (nextDist < dist[nextNode.to]) {
                    dist[nextNode.to] = nextDist;
                    pq.offer(new Node(nextNode.to, nextDist));
                }
            }
        }
        
        int answer = 0;
        for (int i = 0; i <= N; i++) {
            if (dist[i] <= K)
                answer++;
        }

        return answer;
    }
}