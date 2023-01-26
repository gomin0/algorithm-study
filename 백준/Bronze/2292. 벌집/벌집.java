import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        int count = 1; //1겹부터 시작
        int range = 2; //2부터 시작

        if(N == 1) {
            System.out.println(1);
        }else {
            while(range <= N) {
                range = range + (6 * count);
                count++;
            }
            System.out.println(count);
        }

    }
}