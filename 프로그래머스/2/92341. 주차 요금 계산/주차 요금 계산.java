import java.util.*;

class Solution {
    public int[] solution(int[] fees, String[] records) {
        Map<Integer, List<Integer>> record = new HashMap<>();
        Map<Integer, Integer> price = new HashMap<>();
        
        for(String r : records) {
            String[] parts = r.split(" ");
            String[] time = parts[0].split(":");
            int h = Integer.parseInt(time[0]);
            int m = Integer.parseInt(time[1]);
            int t = h * 60 + m;
            int car = Integer.parseInt(parts[1]);
            if (!record.containsKey(car))
                record.put(car, new ArrayList<>());
            record.get(car).add(t);
        }
        
        int idx = 0;
        int[] carNum = new int[record.size()];
        for (int num : record.keySet()) {
            carNum[idx] = num;
            int total = 0;
            List<Integer> times = record.get(num);
            for (int i = 0; i < times.size(); i++) {
                if (i % 2 == 0)
                    total -= times.get(i);
                else
                    total += times.get(i);
            }
            if (times.size() % 2 == 1)
                total += 23 * 60 + 59;
            idx++;
            int totalP = totalPrice(total, fees);
            price.put(num, totalP);
        }
        
        Arrays.sort(carNum);
        int[] answer = new int[carNum.length];
        int i = 0;
        for (int n : carNum) {
            answer[i] = price.get(n);
            i++;
        }
        
        return answer;
    }
    
    private int totalPrice(int time, int[] fees) {
        int price = fees[1];        
        if (time <= fees[0])
            return price;
        price += Math.ceil((time - fees[0]) / (double) fees[2]) * fees[3];
        return price;
    }
}