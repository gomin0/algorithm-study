import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    static final int M = 1234567891;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int L = Integer.parseInt(br.readLine());
        String str = new String(br.readLine());
        long sum = 0;
        long r = 1;

        for(int i = 0; i < L; i++) {
            sum += ((str.charAt(i) - 'a' + 1) * r) % M;
            r = (r * 31) % M;
        }
        System.out.println(sum % M);
    }
}