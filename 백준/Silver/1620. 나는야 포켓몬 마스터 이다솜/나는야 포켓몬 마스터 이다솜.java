import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        Map<String, Integer> map1 = new HashMap<>(); // 이름으로 번호를 찾을 Map
        Map<Integer, String> map2 = new HashMap<>(); // 번호로 이름을 찾을 Map

        for (int i = 1; i <= n; i++) {
            String name = br.readLine();
            map1.put(name, i);
            map2.put(i, name);
        }

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < m; i++) {
            String input = br.readLine();
            if (Character.isDigit(input.charAt(0))) { // 입력이 숫자인 경우
                int num = Integer.parseInt(input);
                sb.append(map2.get(num)).append("\n");
            } else { // 입력이 문자열인 경우
                sb.append(map1.get(input)).append("\n");
            }
        }

        System.out.println(sb);
    }
}