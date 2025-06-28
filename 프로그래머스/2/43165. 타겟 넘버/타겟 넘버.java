class Solution {
    static int answer = 0;
    public int solution(int[] numbers, int target) {
        dfs(0, numbers, target, 0);        
        return answer;
    }
    
    private void dfs(int depth, int[] numbers, int target, int num) {
        if (depth == numbers.length){
            if (num == target)
                answer++;
            return;
        }
        int plus = num + numbers[depth];
        int minus = num - numbers[depth];
        
        dfs(depth + 1, numbers, target, plus);
        dfs(depth + 1, numbers, target, minus);
    }
}