class Solution {
    public int[] solution(int[] prices) {
        int len = prices.length;
        int[] answer = new int[len];
        
        for (int i=0; i<len; i++) {
            int price = prices[i];
            int count = -1;
            for (int j=i; j<len; j++) {
                int nPrice = prices[j];
                if (price <= nPrice)
                    count++;
                else {
                    count++;
                    break;
                }
            }
            answer[i] = count;
        }
        return answer;
    }
}