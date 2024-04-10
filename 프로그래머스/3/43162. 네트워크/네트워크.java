//bfs
import java.util.*;
class Solution {
    static boolean visited[];
    public int solution(int n, int[][] computers) {
        int answer = 0;
        visited = new boolean[n];
        
        for (int i = 0; i < n; i++) {
            if(visited[i] == false) {
                bfs(i, computers, n);
                answer++;
            }
        }
        return answer;
    }
    static void bfs(int i, int[][] computers, int n) {
        Queue<Integer> q = new LinkedList<>();
        q.offer(i);
        visited[i] = true;
        
        while (!q.isEmpty()) {
            int a = q.poll();
            for (int j = 0; j < n; j++) {
                if (visited[j] == false && computers[a][j] == 1) {
                    visited[j] = true;
                    q.offer(j);
                }
            }
        }
    }
}

//dfs
// class Solution {
//     static boolean visited[];    
//     public int solution(int n, int[][] computers) {
//         int answer = 0;
//         visited = new boolean[n];
        
//         for (int i = 0; i < n; i++) {
//             if (visited[i] == false) {
//                 answer++;
//                 dfs(i, computers, n);
//             }
//         }
//         return answer;
//     }
    
//     static void dfs(int i, int[][] computers, int n) {
//         visited[i] = true;
//         for (int j = 0; j < n; j++) {
//             if (visited[j] == false && computers[i][j] == 1) {
//                 dfs(j, computers, n);
//             }
//         }
//     }
// }