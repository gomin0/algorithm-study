class Solution {
    public int[] solution(int brown, int yellow) {
        int a = 0;
        int b = 0;
        int row = 0;
        int column = 0;
        for (int i = 1; i <= yellow; i++) {
            if(yellow % i == 0) {
                a = i;
                b = yellow / a;
                System.out.println("a = " + a);
                System.out.println("b = " + b);
            }
            if (2*(a+b+2) == brown) {
                row = b;
                column = a;
                System.out.println("row = " + row);
                System.out.println("column = " + column);
                break;
            }
        }

        int[] answer = {row + 2, column + 2};
        return answer;
    }
}