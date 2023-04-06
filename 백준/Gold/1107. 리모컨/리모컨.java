import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int n, m;
    static boolean[] broken = new boolean[10];

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        // 채널 번호 n 입력
        n = Integer.parseInt(br.readLine());

        // 고장난 버튼 개수 m 입력
        m = Integer.parseInt(br.readLine());

        // 고장난 버튼 표시
        if (m > 0) {
            st = new StringTokenizer(br.readLine());
            for (int i = 0; i < m; i++) {
                int btn = Integer.parseInt(st.nextToken());
                broken[btn] = true;
            }
        }

        int ans = Math.abs(n - 100); // 초기값 설정

        // 0 ~ 1000000 사이의 모든 채널을 탐색
        for (int i = 0; i <= 1000000; i++) {
            int channel = i;
            int cnt = possible(channel); // 이동 가능한 채널인지 체크

            if (cnt > 0) { // 이동 가능 하면
                int press = Math.abs(channel - n); // +,- 버튼을 몇 번 눌러야 하는지 계산
                ans = Math.min(ans, cnt + press); // 최소값 갱신
            }
        }

        System.out.println(ans);
    }

    // 해당 채널로 이동할 수 있는지 체크하는 함수
    public static int possible(int channel) {
        if (channel == 0) {
            if (broken[0]) {
                return 0;
            } else {
                return 1;
            }
        }
        int len = 0;
        while (channel > 0) {
            if (broken[channel % 10]) {
                return 0;
            }
            len++;
            channel /= 10;
        }
        return len;
    }
}