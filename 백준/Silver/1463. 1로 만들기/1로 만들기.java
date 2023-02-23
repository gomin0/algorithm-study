import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int X = Integer.parseInt(br.readLine());
        System.out.println(recur(X, 0));
    }

    static int recur(int X, int count) {
        if(X < 2) {
            return count;
        }
        return Math.min(recur(X / 2, count + 1 + (X % 2)), (recur(X / 3, count + 1 + (X % 3))));
    }
}