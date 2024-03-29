import java.util.*;
class Solution {
    public boolean solution(String[] phone_book) {
    //     Arrays.sort(phone_book);
    //     for(int i = 0; i < phone_book.length; i++) {
    //         for(int j = i + 1; j < phone_book.length; j++) {
    //             if (phone_book[j].startsWith(phone_book[i])) {
    //                 return false;
    //             }
    //         }
    //     }
    //     return true;
    // }
        Map<String, Integer> map = new HashMap<>();
        
        for (int i = 0; i < phone_book.length; i++) {
            map.put(phone_book[i], i);
        }
        
        for (int i = 0; i < phone_book.length; i++) {
            for (int j = 0; j < phone_book[i].length(); j++) {
                if (map.containsKey(phone_book[i].substring(0,j))) {
                    return false;
                }
            }
        }
        return true;
    }
}