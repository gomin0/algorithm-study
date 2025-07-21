import java.util.*;

class Solution {
    public String[] solution(String[] record) {
        Map<String, String> user = new HashMap<>();
        List<String> action = new ArrayList<>();
        List<String> userId = new ArrayList<>();
        
        for (String r : record) {
            String[] parts = r.split(" ");
            String act = parts[0];
            String uid = parts[1];
            if (!act.equals("Change")) {
                action.add(act);
                userId.add(uid);
            }
            if (parts.length == 3) {
                String name = parts[2];
                user.put(uid, name);
            }
        }
        
        int size = action.size();
        String[] answer = new String[size];
        for (int i = 0; i < size; i++) {
            String userName = user.get(userId.get(i));
            String result = userName + "님이 ";
            if (action.get(i).equals("Enter"))
                result += "들어왔습니다.";
            else
                result += "나갔습니다.";
            answer[i] = result;
        }
        
        return answer;
    }
}