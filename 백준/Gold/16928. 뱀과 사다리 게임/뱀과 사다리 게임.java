import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
    static int[] map = new int[101]; // 맵
    static boolean[] visited = new boolean[101]; // 방문 체크
    static int ladderNum, snakeNum;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        ladderNum = Integer.parseInt(st.nextToken());
        snakeNum = Integer.parseInt(st.nextToken());

        for (int i = 0; i < ladderNum + snakeNum; i++) {
            st = new StringTokenizer(br.readLine());
            map[Integer.parseInt(st.nextToken())] = Integer.parseInt(st.nextToken()); // 뱀과 사다리 정보 넣기
        }

        Queue<Integer> queue = new LinkedList<>();

        queue.add(1); // 시작점
        visited[1] = true;

        int count = 0; // 횟수
        boolean find = false;

        while (!queue.isEmpty()) {
            int size = queue.size();

            for (int i = 0; i < size; i++) {
                int now = queue.poll();

                if (now == 100) {
                    find = true;
                    break;
                }

                for (int j = 1; j <= 6; j++) {
                    // 100번 칸 이하로 이동 가능
                    if (now + j <= 100) {

                        int next = now + j;

                        // 사다리나 뱀이 있는 경우 타고 이동
                        if (map[next] > 0) {
                            next = map[next];
                        }

                        // 이전에 방문하지 않았던 경우만 이동
                        if (!visited[next]) {
                            visited[next] = true;
                            queue.add(next);
                        }
                    }
                }
            }
            if (find)
                break;

            count++;
        }

        System.out.println(count);
    }
}