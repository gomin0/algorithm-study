class Solution {
    public int solution(int[] stones, int k) {
        int maxStone = 0;
        for (int stone : stones) if (stone > maxStone) maxStone = stone;
        int left = 1;
        int right = maxStone;
        
        while (left <= right) {
            int mid = (left + right) / 2;
            int count = 0;
            boolean possible = true;
            for (int stone : stones) {
                if (stone < mid) count ++;
                else count = 0;
                if (count >= k) {
                    right = mid-1;
                    possible = false;
                    break;
                }
            }
            if (possible) left = mid+1;
        }
        return right;
    }
}