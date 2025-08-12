import java.util.*;

class Solution {
    static class Node implements Comparable<Node> {
        int to, cost;
        
        Node(int to, int cost) {
            this.to = to;
            this.cost = cost;
        }
        
        @Override
        public int compareTo(Node n) {
            return this.cost - n.cost;
        }
    }
    
    public int solution(int N, int[][] road, int K) {
        List<List<Node>> graph = new ArrayList<>();
        for (int i = 0; i <= N; i++) {
            graph.add(new ArrayList<>());
        }
        
        for (int[] info : road) {
            int a = info[0], b = info[1], d = info[2];
            graph.get(a).add(new Node(b, d));
            graph.get(b).add(new Node(a, d));
        }
        
        int[] dist = new int[N+1];
        Arrays.fill(dist, Integer.MAX_VALUE);
        dist[1] = 0;
        
        PriorityQueue<Node> pq = new PriorityQueue<>();
        pq.offer(new Node(1, 0));
        
        while (!pq.isEmpty()) {
            Node node = pq.poll();
            if (node.cost > dist[node.to]) continue;
            for (Node nextNode : graph.get(node.to)) {
                int nextCost = node.cost + nextNode.cost;
                if (dist[nextNode.to] > nextCost) {
                    dist[nextNode.to] = nextCost;
                    pq.offer(new Node(nextNode.to, nextCost));
                }
            }
        }
        
        int answer = 0;
        for (int i = 0; i <= N; i++)
            if (dist[i] <= K) answer++;
        return answer;
    }
}