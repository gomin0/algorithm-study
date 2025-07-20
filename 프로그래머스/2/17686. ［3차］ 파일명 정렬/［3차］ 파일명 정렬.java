import java.util.*;

class Solution {
    
    static class FilePart {
        String head;
        int number;
        String original;
        
        public FilePart(String head, int number, String original) {
            this.head = head;
            this.number = number;
            this.original = original;
        }
    }
    
    public String[] solution(String[] files) {
        List<FilePart> fileParts = new ArrayList<>();
        
        for (String file : files) {
            String head = "";
            String number = "";

            int i = 0;
            while (i < file.length() && !Character.isDigit(file.charAt(i))) {
                head += file.charAt(i);
                i++;
            }
            
            int j = i;
            while (
                i < file.length() && Character.isDigit(file.charAt(i)) && i - j < 55
            ) {
                number += file.charAt(i);
                i++;
            }
            
            fileParts.add(new FilePart(head, Integer.parseInt(number), file));
        }
        
        fileParts.sort((f1, f2) -> {
            int headCompare = f1.head.toLowerCase().compareTo(f2.head.toLowerCase());
            if (headCompare != 0) return headCompare;
            return Integer.compare(f1.number, f2.number);
        });
        
        String[] answer = new String[files.length];
        for (int i = 0; i < fileParts.size(); i++) {
            answer[i] = fileParts.get(i).original;
        }
            
        return answer;
    }
}