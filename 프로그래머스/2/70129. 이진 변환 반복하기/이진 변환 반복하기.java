class Solution {
    public int[] solution(String s) {
        int[] answer = new int[2];
        int count = 0;
        int times = 0;
        while (!s.equals("1")) {
            for (char c : s.toCharArray()) {
                if (c == '0')
                    count ++;
            }
            s = s.replace("0", "");
            int len = s.length();
            s = Integer.toBinaryString(len);
            times ++;
        }
        answer[0] = times;
        answer[1] = count;
        return answer;
    }
}