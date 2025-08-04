import java.util.*;

class Solution {
    public int solution(String[][] book_time) {
        List<int[]> times = new ArrayList<>();
        PriorityQueue<Integer> room = new PriorityQueue<>();
        for (String[] bt : book_time) {
            String startTime = bt[0];
            String endTime = bt[1];
            times.add(new int[]{timeToMinute(startTime), timeToMinute(endTime) + 10});
        }
        times.sort((a, b) -> a[0] - b[0]);
        
        int answer = 0;
        for (int[] time : times) {
            int start = time[0];
            int end = time[1];
            if (room.isEmpty()) {
                answer++;
                room.add(end);
                continue;
            }
            int t = room.peek();
            if (t <= start)
                room.poll();
            else
                answer++;
            room.add(end);
        }
        
        return answer;
    }
    
    private int timeToMinute(String time) {
        String[] times = time.split(":");
        int hour = Integer.parseInt(times[0]) * 60;
        int minute = Integer.parseInt(times[1]);
        return hour + minute;
    }
}