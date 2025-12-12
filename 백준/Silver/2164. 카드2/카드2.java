import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        Queue<Integer> q = new LinkedList<>();
        int n = sc.nextInt();
        
        for (int i =1;i<=n;i++){
            q.add(i);
        }
        
        while(q.size()>1){
            q.poll();
            q.add(q.poll());
        }
        System.out.println(q.poll()); //마지막 남은 카드 출력
    }
}