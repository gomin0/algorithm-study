class Solution {
    private int zero = 0;
    private int one = 0;
    
    public int[] solution(int[][] arr) {
        int n = arr.length;
        compress(arr, 0, 0, n);
        int[] answer = new int[]{zero, one};
        return answer;
    }
    
    private void compress(int[][] arr, int x, int y, int size) {
        if (isSame(arr, x, y, size)) {
            if (arr[x][y] == 0)
                zero++;
            else
                one++;
            return;
        }
        
        int half = size / 2;
        
        compress(arr, x, y, half);
        compress(arr, x, y + half, half);
        compress(arr, x + half, y, half);
        compress(arr, x + half, y + half, half);
    }
    
    private boolean isSame(int[][] arr, int x, int y, int size) {
        int num = arr[x][y];
        for (int i = x; i < x + size; i++) {
            for (int j = y; j < y + size; j++) {
                if (arr[i][j] != num)
                    return false;
            }
        }
        return true;
    }
}