class Solution {
    public String solution(String p) {
        if (p.equals("")) return "";
        if (isValid(p)) return p;
        String answer = "";
        
        String[] split = splitString(p);
        String u = split[0];
        String v = split[1];
        if (isValid(u)) {
            return u + solution(v);
        }
        else {
            StringBuilder sb = new StringBuilder();
            sb.append("(");
            sb.append(solution(v));
            sb.append(")");
            sb.append(reverse(u.substring(1, u.length()-1)));
            return sb.toString();
        }
    }
    
    private boolean isValid(String s) {
        int count = 0;
        for (char c : s.toCharArray()) {
            if (c == '(') count++;
            else count--;
            if (count < 0) return false;
        }
        if (count == 0) return true;
        else return false;
    }
    
    private String[] splitString(String s) {
        int count = 0;
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '(') count++;
            else count--;
            if (count == 0) {
                String u = s.substring(0, i+1);
                String v = s.substring(i+1);
                return new String[]{u, v};
            }
        }
        return new String[]{s, ""};
    }
    
    private String reverse(String s) {
        StringBuilder sb = new StringBuilder();
        for (char c : s.toCharArray()) {
            if (c == '(') sb.append(')');
            else sb.append('(');
        }
        return sb.toString();
    }
}