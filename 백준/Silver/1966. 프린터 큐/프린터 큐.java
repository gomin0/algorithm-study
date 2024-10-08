import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] ars) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int T = Integer.parseInt(br.readLine());

        for (int t = 0; t < T; t++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int n = Integer.parseInt(st.nextToken());
            int idx = Integer.parseInt(st.nextToken());
            int count = 1;

            Queue<Integer> queue = new LinkedList<>();
            st = new StringTokenizer(br.readLine());
            for (int i = 0; i < n; i++) {
                queue.add(Integer.parseInt(st.nextToken()));
            }

            while (true) {
                int maxPri = findMax(queue);
                int now = queue.poll();

                if (now < maxPri) {
                    queue.add(now);
                    if (idx == 0) {
                        idx = queue.size() - 1;
                    } else {
                        idx--;
                    }
                }
                else {
                    if (idx == 0) {
                        System.out.println(count);
                        break;
                    } else {
                        idx--;
                        count++;
                    }
                }


            }
        }

    }

    public static int findMax(Queue<Integer> queue) {
        int max = 1;

        for (int num : queue) {
            if (num > max) {
                max = num;
            }
        }
        return max;
    }

}