import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Deque;
import java.util.LinkedList;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        Deque<Integer> dq = new LinkedList<>();

        int N = Integer.parseInt(br.readLine());

        for(int i = 1; i <= N; i++) {
            dq.offer(i);
        }

        while (dq.size() > 1) {
            dq.poll();
            dq.offer(dq.poll());
        }
        System.out.println(dq.poll());
    }
}