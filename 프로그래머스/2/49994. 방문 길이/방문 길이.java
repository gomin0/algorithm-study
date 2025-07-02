import java.util.*;

class Solution {
    public int solution(String dirs) {
        int answer = 0;
        Set<String> path = new HashSet<>();
        int x = 0;
        int y = 0;
        int max_x = 5;
        int max_y = 5;
        int min_x = -5;
        int min_y = -5;
        
        for (char d : dirs.toCharArray()) {
            int dx = 0;
            int dy = 0;
            if (d == 'U')
                dy = 1;
            else if (d == 'D')
                dy = -1;
            else if (d == 'R')
                dx = 1;
            else
                dx = -1;
            int nx = x + dx;
            int ny = y + dy;
            if (min_x<=nx && max_x>=nx && min_y<=ny && max_y>=ny) {
                path.add(x+","+y+","+nx+","+ny);
                path.add(nx+","+ny+","+x+","+y);
                x = nx;
                y = ny;
            }
        }
        
        return path.size() / 2;
    }
}