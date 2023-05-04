import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken()); // 저장된 사이트 주소의 수
        int m = Integer.parseInt(st.nextToken()); // 비밀번호를 찾으려는 사이트 주소의 수

        HashMap<String, String> map = new HashMap<>();

        // 저장된 사이트 주소와 비밀번호를 HashMap에 저장
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            String site = st.nextToken();
            String password = st.nextToken();
            map.put(site, password);
        }

        // 비밀번호를 찾으려는 사이트 주소를 입력받고, 해당하는 비밀번호를 출력
        for (int i = 0; i < m; i++) {
            String site = br.readLine();
            System.out.println(map.get(site));
        }
    }
}