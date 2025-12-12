import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        {
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            int N = Integer.parseInt(br.readLine());
            PriorityQueue<Integer> pq = new PriorityQueue<>((o1, o2) ->
            {
                int first = Math.abs(o1);
                int second = Math.abs(o2);

                if (first==second){
                    return o1>o2?1:-1; //음수 기준으로 정렬
                } else
                    /*
                    음수면 우선순위가 높음
                    결과 음수 → o1 먼저
                    결과 양수 → o1 뒤
                     */
                    return first-second; //절댓값 작은걸 앞으로
            });

            for (int i=0;i<N;i++){
                int request = Integer.parseInt(br.readLine());
                if (request == 0){
                    if (pq.isEmpty()){
                        System.out.println("0");
                    } else{
                        System.out.println(pq.poll());
                    }
                }else {
                    pq.add(request);
                }
            }
        }}
}