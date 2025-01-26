import java.util.*;

class Solution {
    public int[] solution(int[] fees, String[] records) {
        Map<String, Integer> inTimeMap = new HashMap<>();
        Map<String, Integer> parkingTimeMap = new HashMap<>();
        
        for (String r : records) {
            String[] record = r.split(" ");
            String time = record[0];
            String carNum = record[1];
            String type = record[2];
            
            int minute = timeToMinute(time);
            
            if (type.equals("IN")) {
                inTimeMap.put(carNum, minute);
            } else {
                int inTime = inTimeMap.remove(carNum);
                int total = minute - inTime;
                total += parkingTimeMap.getOrDefault(carNum, 0);  // 전에 기록 있는지
                parkingTimeMap.put(carNum, total);
            }
        }
        
        for (Map.Entry<String, Integer> entry : inTimeMap.entrySet()) {
            String carNum = entry.getKey();
            int inTime = entry.getValue();
            int total = timeToMinute("23:59") - inTime;
            total += parkingTimeMap.getOrDefault(carNum, 0);
            parkingTimeMap.put(carNum, total);
        }
        
        List<String> cars = new ArrayList<>(parkingTimeMap.keySet());
        Collections.sort(cars);
        
        int[] answer = new int[cars.size()];
        for (int i = 0; i < cars.size(); i++) {
            String carNum = cars.get(i);
            int time = parkingTimeMap.get(carNum);
            answer[i] = totalFee(time, fees);
        }
        
        return answer;
    }
    
    private int timeToMinute(String time) {
        String[] t = time.split(":");
        int h = Integer.parseInt(t[0]);
        int m = Integer.parseInt(t[1]);
        
        return h*60 + m;
    }
    
    private int totalFee(int time, int[] fees) {
        int baseTime = fees[0];
        int baseFee = fees[1];
        int unitTime = fees[2];
        int unitFee = fees[3];
        
        if (time <= baseTime) {
            return baseFee;
        }
        
        int extraTime = time - baseTime;
        int extraFee = (int) Math.ceil((double) extraTime / unitTime) * unitFee;
        
        return baseFee + extraFee;
    }
}