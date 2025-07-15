import java.util.*;

class Solution {
    public int solution(String skill, String[] skill_trees) {
        Set<Character> possibleSkills = new HashSet<>();
        Map<Character, Character> preSkill = new HashMap<>();
        for (char c = 'A'; c <= 'Z'; c++)
            possibleSkills.add(c);
        for (int i = 1; i < skill.length(); i++) {
            possibleSkills.remove(skill.charAt(i));
            preSkill.put(skill.charAt(i-1), skill.charAt(i));
        }
        
        int answer = 0;
        for (String skills : skill_trees) {
            boolean possible = true;
            Set<Character> nowPossibleSkills = new HashSet<>(possibleSkills);
            for (char s : skills.toCharArray()) {
                if (!nowPossibleSkills.contains(s)) {
                    possible = false;
                    break;
                }
                if (preSkill.containsKey(s))
                    nowPossibleSkills.add(preSkill.get(s));
            }
            if (possible){
                answer++;
            }
        }
        
        return answer;
    }
}