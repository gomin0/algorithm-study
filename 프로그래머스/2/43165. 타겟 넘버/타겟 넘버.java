class Solution {
    static int answer = 0;
    public int solution(int[] numbers, int target) {
        dfs(0, numbers, target, 0);
        return answer;
    }
    
    static void dfs(int depth, int[] numbers, int target, int result) {
        if (depth == numbers.length) {
            if (target == result) {
                answer++;
            }
            return;
        }
        
        int plus = result + numbers[depth];
        int minus = result - numbers[depth];
        
        dfs (depth + 1, numbers, target, plus);
        dfs (depth + 1, numbers, target, minus);
    }
}