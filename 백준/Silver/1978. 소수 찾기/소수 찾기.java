import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        boolean arr[] = new boolean[1001];
        int count = 0;

        arr[0] = arr[1] = true;

        for(int i = 2; i*i< 1001; i++) {
            if(arr[i]) continue;
            for(int j = i * i; j < 1001; j += i) {
                arr[j] = true;
            }
        }

        StringTokenizer st = new StringTokenizer(br.readLine()," ");
       for(int i = 0; i < N; i++) {
           int num = Integer.parseInt(st.nextToken());
           if(!arr[num]) count++;
       }
       System.out.println(count);
    }

}