class Solution {
    public long[] solution(long[] numbers) {
        long[] answer = new long[numbers.length];
        int idx = 0;
        for (long number : numbers) {
            String bin = "";
            if (number % 2 == 0) {
                answer[idx] = number + 1;
            }
            else {
                String binString = "0" + Long.toBinaryString(number);
                char[] arr = binString.toCharArray();
                for (int i = arr.length - 1; i > 0; i--) {
                    if (arr[i-1] == '0' && arr[i] == '1') {
                        arr[i-1] = '1';
                        arr[i] = '0';
                        break;
                    }
                }
                long result = Long.parseLong(new String(arr), 2);
                answer[idx] = result;
            }
            idx++;
        }
        return answer;
    }
}