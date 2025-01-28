import java.util.*;

class Solution {
    public ArrayList<String> solution(String[] record) {        
        Map<String, String> name = new HashMap<>();
        ArrayList<String> answer = new ArrayList<>();

        for (String r : record) {
            String[] parts = r.split(" ");
            String command = parts[0];
            String uid = parts[1];
            if (!command.equals("Leave")) {
                String nickname = parts[2];
                name.put(uid, nickname);
            }
        }
        
        for (String r : record) {
            String[] parts = r.split(" ");
            String command = parts[0];
            String uid = parts[1];
            String nickname = name.get(uid);
            
            if (command.equals("Enter")) {
                answer.add(nickname + "님이 들어왔습니다.");
            } else if (command.equals("Leave")) {
                answer.add(nickname + "님이 나갔습니다.");
            }
        }
        
        return answer;
    }
}