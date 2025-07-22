class Solution {
    public int solution(int m, int n, String[] board) {
        char[][] map = new char[m][n];
        for (int i = 0; i < m; i++)
            map[i] = board[i].toCharArray();
        
        int remove = 0;
        while (true) {
            boolean[][] marked = new boolean[m][n];
            boolean match = false;
            
            for (int i = 0; i < m-1; i++) {
                for (int j = 0; j < n-1; j++) {
                    char current = map[i][j];
                    if (current == ' ') 
                        continue;
                    if (
                        map[i][j+1] == current &&
                        map[i+1][j] == current &&
                        map[i+1][j+1] == current
                    ) {
                        marked[i][j] = true;
                        marked[i+1][j] = true;
                        marked[i][j+1] = true;
                        marked[i+1][j+1] = true;
                        match = true;
                    }
                }
            }
            if (!match)
                break;
            for (int i = 0; i < m; i++) {
                for (int j = 0; j < n; j++) {
                    if (marked[i][j]) {
                        map[i][j] = ' ';
                        remove++;
                    }
                }
            }
            for (int j = 0; j < n; j++) {
                for (int i = m-1; i >= 0; i--) {
                    if (map[i][j] == ' ') {
                        int k = i - 1;
                        while (k >= 0 && map[k][j] == ' ') {
                            k--;
                        }
                        if (k >= 0) {
                            map[i][j] = map[k][j];
                            map[k][j] = ' ';
                        }
                    }
                }
            }
        }
        
        return remove;
    }
}