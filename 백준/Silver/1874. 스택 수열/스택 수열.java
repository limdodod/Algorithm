import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Stack;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine()); // 숫자 개수
        int []A = new int[N];

        for (int i=0;i<N;i++){
            A[i] = Integer.parseInt(br.readLine());
        }

        Stack<Integer> stack = new Stack<>();
        StringBuffer bf = new StringBuffer();

        int num = 1;
        boolean result = true;

        for (int i =0;i<A.length;i++){
            int now = A[i];
            if (now>=num) { // 입력한 수가 오름차순 자연수보다 크거나 같을 때 
                while (now >= num) {
                    stack.push(num++);
                    bf.append("+\n");
                }
                stack.pop();
                bf.append("-\n");
            } else{     // 입력한 수가 오름차순 자연수보다 작을 때 
                int n = stack.pop();
                if (n>now){ //스택의 맨 위가 입력한 수보다 클 때 
                    System.out.println("NO");
                    result = false;
                    break;
                }
                else{
                    bf.append("-\n");
                }
            }
        }
        if (result){System.out.println(bf.toString());}
    }
}