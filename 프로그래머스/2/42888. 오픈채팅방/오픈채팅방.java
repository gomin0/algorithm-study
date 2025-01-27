import java.util.*;

class Solution {
    public String[] solution(String[] record) {        
        Map<String, String> name = new HashMap<>();
        List<String[]> messages = new ArrayList<>();

        for (String r : record) {
            String[] parts = r.split(" ");
            String command = parts[0];
            String uid = parts[1];
            
            if (command.equals("Enter")) {
                String nickname = parts[2];
                name.put(uid, nickname);
                messages.add(new String[]{uid, "님이 들어왔습니다."});
            } else if (command.equals("Leave")) {
                messages.add(new String[]{uid, "님이 나갔습니다."});
            } else {
                String nickname = parts[2];
                name.put(uid, nickname);
            }
        }
        
        String[] answer = new String[messages.size()];
        int idx = 0;
        for (String[] message : messages) {
            String userId = message[0];
            String action = message[1];
            String nickname = name.get(userId);
            answer[idx++] = nickname+action;
        }
        
        return answer;
    }
}