class Solution {
    public long solution(int price, int money, int count) {
        
        int time = 1;
        long total_price = 0;
        for (int i = 0; i < count; i++) {
            total_price += price * time;
            time++;
        }
        
        if (total_price > money) {
            return total_price - money;
        } else {
            return 0;
        }
    }
}