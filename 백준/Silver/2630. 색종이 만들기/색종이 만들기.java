import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int[][] paper; // 색종이 배열
    static int[] count = new int[2]; // 색종이 개수를 저장하는 배열

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine()); // 색종이 배열 크기
        paper = new int[n][n];

        // 색종이 배열 초기화
        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                paper[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        cutPaper(0, 0, n); // 색종이 자르기

        System.out.println(count[0]); // 흰색 색종이 개수 출력
        System.out.println(count[1]); // 파란색 색종이 개수 출력
    }

    static void cutPaper(int x, int y, int size) {
        if (checkPaper(x, y, size)) { // 모두 같은 색종이인 경우
            count[paper[x][y]]++; // 색종이 개수 증가
        } else { // 색종이가 같지 않은 경우
            int newSize = size / 2;
            cutPaper(x, y, newSize); // 왼쪽 위
            cutPaper(x + newSize, y, newSize); // 오른쪽 위
            cutPaper(x, y + newSize, newSize); // 왼쪽 아래
            cutPaper(x + newSize, y + newSize, newSize); // 오른쪽 아래
        }
    }

    static boolean checkPaper(int x, int y, int size) {
        int color = paper[x][y]; // 첫번째 칸의 색종이
        for (int i = x; i < x + size; i++) {
            for (int j = y; j < y + size; j++) {
                if (paper[i][j] != color) { // 색종이가 다른 경우
                    return false;
                }
            }
        }
        return true; // 모두 같은 색종이인 경우
    }
}