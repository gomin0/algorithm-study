class Solution {
    public long solution(int n, int[] times) {
        long minTime = Long.MAX_VALUE;
        for (long time : times) {
            if (time < minTime) minTime = time;
        }
        
        long left = 0L;
        long right = (long) minTime * n;
        long answer = 0;
        while (left <= right) {
            long mid = (long) (left + right) / 2;
            
            if (can(mid, times, n)) {
                answer = mid;
                right = mid - 1;
            } else left = mid + 1;
            
        }
        return answer;
    }
    
    private boolean can(long mid, int[] times, long n) {
        long done = 0L;
        for (int time : times) {
            done += mid / time;
            if (done >= n) return true;
        }
        return false;
    }
}