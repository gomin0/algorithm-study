import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    static int count;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int r = Integer.parseInt(st.nextToken());
        int c = Integer.parseInt(st.nextToken());
        int size = (int) Math.pow(2, N);

        countZ(size, r, c);
        System.out.println(count);
    }

    private static void countZ(int size, int r, int c) {
        if(size == 1)
            return;

        int s = size / 2; //2^(n-1) 크기

        if(r < s && c < s) { //1사분면
            countZ(s, r, c);
        }
        else if(r < s && c < 2 * s) { //2사분면
            count += s * s; // 1사분면 count
            countZ(s, r, c - s);
        }
        else if(r < 2 * s && c < s) { //3사분면
            count += s * s * 2; // 1, 2사분면 count
            countZ(s, r - s, c);
        }
        else if(r < s * 2 && c < s * 2) { //4사분면
            count += s * s * 3; //1, 2, 3사분면 count
            countZ(s, r - s, c - s);
        }
    }
}