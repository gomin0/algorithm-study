class Solution {
    public boolean solution(int x) {
        int num = 0;
        int nx = x;
        while (nx > 0) {
            num += nx % 10;
            nx /= 10;
        }
        
        if (x % num == 0) {
            return true;
        }
        else {
            return false;
        }
            
    }
}