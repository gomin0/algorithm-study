class Solution {
    public int solution(String[] babbling) {
        int answer = 0;
        
        for (String word : babbling) {
            boolean isValid = true;
            String prevWord = "";
            int pointer = 0;
            
            while (pointer < word.length()) {
                if (prevWord != "aya" && (pointer + 3 <= word.length()) && word.charAt(pointer) == 'a' && word.charAt(pointer+1) == 'y' && word.charAt(pointer+2) == 'a') {
                    pointer += 3;
                    prevWord = "aya";
                }
                else if (prevWord != "ye" && (pointer + 2 <= word.length()) && word.charAt(pointer) == 'y' && word.charAt(pointer+1) == 'e') {
                    pointer += 2;
                    prevWord = "ye";
                }
                else if (prevWord != "woo" && (pointer + 3 <= word.length()) && word.charAt(pointer) == 'w' && word.charAt(pointer+1) == 'o' && word.charAt(pointer+2) == 'o') {
                    pointer += 3;
                    prevWord = "woo";
                }
                else if (prevWord != "ma" && (pointer + 2 <= word.length()) && word.charAt(pointer) == 'm' && word.charAt(pointer+1) == 'a') {
                    pointer += 2;
                    prevWord = "ma";
                }
                else {
                    isValid = false;
                    break;
                }
            }
            
            if (isValid) {
                answer++;
            }
        }
        
        return answer;
    }
}