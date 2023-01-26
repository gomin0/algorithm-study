import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int B = Integer.parseInt(st.nextToken());

        int arr[][] = new int[N][M];
        int low = 256;
        int high = 0;

        for(int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for(int j = 0; j < M; j++) {
                arr[i][j] = Integer.parseInt(st.nextToken());
                if(arr[i][j] < low) {
                    low = arr[i][j];
                }
                if(arr[i][j] > high) {
                    high = arr[i][j];
                }
            }
        }

        int min_time = 100000000;
        int ground = 0;

        for(int i = low; i <= high; i++) {
            int time = 0;
            int block = B;
            for(int a = 0; a < N; a++) {
                for(int b = 0; b < M; b++) {
                    if(i < arr[a][b]) {
                        time += ((arr[a][b] - i) * 2);
                        block += arr[a][b] - i;
                    }else {
                        time += i - arr[a][b];
                        block -= i - arr[a][b];
                    }
                }
            }
            if(block < 0) {
                break;
            }
            if(min_time >= time) {
                min_time = time;
                ground = i;
            }
        }

        System.out.println(min_time + " " + ground);

    }
}