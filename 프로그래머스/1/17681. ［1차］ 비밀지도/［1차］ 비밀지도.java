class Solution {
    public String[] solution(int n, int[] arr1, int[] arr2) {
        String[] answer = new String[n];
        
        for (int i = 0; i < arr1.length; i++) {
            String binary = Integer.toString(arr1[i] | arr2[i], 2);
            binary = String.format("%" + n + "s", binary).replace(' ', '0');
            answer[i] = binary.replace('1', '#').replace('0', ' ');
        }
        
        return answer;
    }
}