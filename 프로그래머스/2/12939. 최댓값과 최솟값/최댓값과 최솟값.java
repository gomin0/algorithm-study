class Solution {
    public String solution(String s) {
        String answer = "";
        String [] nums = s.split(" ");
        int min, max;
        min = max = Integer.parseInt(nums[0]);
        
        for (int i = 1; i < nums.length; i++) {
            int num = Integer.parseInt(nums[i]);
            if (num > max) {
                max = num;
            }
            if (num < min) {
                min = num;
            }
        }
        
        answer = min + " " + max;
        
        return answer;
    }
}