class Solution {
    public String solution(String s) {
        StringBuilder answer = new StringBuilder();
        boolean isStart = true;

        for (char c : s.toCharArray()) {
            if (isStart) {
                if (Character.isLetter(c)) {
                    answer.append(Character.toUpperCase(c));
                } else {
                    answer.append(c);
                }
                isStart = false;
            } else {
                answer.append(Character.toLowerCase(c));
            }

            if (c == ' ') {
                isStart = true;
            }
        }

        return answer.toString();
    }
}