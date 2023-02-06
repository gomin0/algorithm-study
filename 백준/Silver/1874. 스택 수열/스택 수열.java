import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int n = Integer.parseInt(br.readLine());
        int[] stack = new int[n];
        int index = 0;
        int start = 0;

        while (n-- > 0){
            int num = Integer.parseInt(br.readLine());
            if(num > start) {
                for(int i = start + 1; i <= num; i++) {
                    stack[index] = i;
                    index++;
                    sb.append('+').append('\n');
                }
                start = num;
            }
            else if(stack[index - 1] != num) {
                System.out.println("NO");
                return;
            }
            index--;
            sb.append('-').append('\n');

        }
        System.out.println(sb);

    }
}