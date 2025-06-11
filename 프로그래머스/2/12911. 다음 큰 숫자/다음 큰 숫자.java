class Solution {
    public int solution(int n) {
        int num = n;
        int nOneCount = countOneInBinary(n);
        while (true) {
            num++;
            int numOneCount = countOneInBinary(num);
            if (nOneCount == numOneCount)
                break;
        }
        return num;
    }
    
    private int countOneInBinary(int num) {
        String numToBinary = Integer.toBinaryString(num);
        int numOneCount = 0;
        for (int i = 0; i < numToBinary.length(); i++) {
            if (numToBinary.charAt(i) == '1')
                numOneCount ++;
        }
        return numOneCount;
    }
}