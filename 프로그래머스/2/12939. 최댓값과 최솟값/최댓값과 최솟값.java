class Solution {
    public String solution(String s) {
        String [] nums = s.split(" ");
        int min, max, n;
        min = max = Integer.parseInt(nums[0]);
        
        for (int i = 1; i < nums.length; i++) {
            n = Integer.parseInt(nums[i]);
            if (min > n) min = n;
            if (max < n) max = n;
        }
        
        return min + " " + max;
    }
}