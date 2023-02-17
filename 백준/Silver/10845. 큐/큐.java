import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        Queue<Integer> q = new LinkedList<>();

        int N = Integer.parseInt(br.readLine());
        int num = 0;

        for(int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            String S = st.nextToken();

            switch (S) {
                case "push":
                    num = Integer.parseInt(st.nextToken());
                    q.offer(num);
                    break;
                case "pop":
                    if(q.size() == 0) {
                        sb.append(-1).append('\n');
                    }else {
                        sb.append(q.poll()).append('\n');
                    }
                    break;
                case "size":
                    sb.append(q.size()).append('\n');
                    break;
                case "empty":
                    if(q.size() == 0) {
                        sb.append(1).append('\n');
                    }else {
                        sb.append(0).append('\n');
                    }
                    break;
                case "front":
                    if(q.size() == 0) {
                        sb.append(-1).append('\n');
                    }else {
                        sb.append(q.peek()).append('\n');
                    }
                    break;
                case "back":
                    if(q.size() == 0) {
                        sb.append(-1).append('\n');
                    }else {
                        sb.append(num).append('\n');
                    }
                    break;
            }
        }
        System.out.println(sb);
    }
}