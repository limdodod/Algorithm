import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int a = Integer.parseInt(st.nextToken()); //2차원 배열 크기
        int b = Integer.parseInt(st.nextToken()); //구간합 질의 개수

        int A[][] = new int[a+1][a+1];
        for (int i=1;i<=a;i++){
            st = new StringTokenizer(br.readLine());
            for (int j=1;j<=a;j++){
                A[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        // 합배열
        int D[][] = new int[a+1][a+1];
        for (int i=1; i<a+1; i++){
            for (int j=1; j<a+1; j++){
                D[i][j] = D[i-1][j] + D[i][j-1]- D[i-1][j-1] + A[i][j];
            }

        }

        //질의 계산
        for (int i=0;i<b;i++){
            st = new StringTokenizer(br.readLine());
            int start1 = Integer.parseInt(st.nextToken());
            int end1 =  Integer.parseInt(st.nextToken());
            int start2 = Integer.parseInt(st.nextToken());
            int end2 =  Integer.parseInt(st.nextToken());

            int result = D[start2][end2]-D[start1-1][end2]- D[start2][end1-1]+ D[start1-1][end1-1];
            System.out.println(result);
        }
    }
}