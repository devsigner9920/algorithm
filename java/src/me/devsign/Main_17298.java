package me.devsign;

import java.io.*;
import java.util.Stack;

public class Main_17298 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = Integer.parseInt(br.readLine());
        String[] arr = br.readLine().split(" ");

        Stack<Integer> stack = new Stack<>();
        String[] result = new String[n];
        for(int i = 0; i < n; ++i) {
            result[i] = "-1";
        }

        for(int i = 0; i < n; i++) {
            if(!stack.empty()) {
                while(!stack.empty()) {
                    int beforeNum = Integer.parseInt(arr[stack.peek()]);
                    if(beforeNum < Integer.parseInt(arr[i])) {
                        result[stack.pop()] = arr[i];
                    } else break;
                }
            }
            stack.add(i);
        }

        for(int i = 0; i < n; ++i) {
            bw.write(result[i]);
            if(i != n - 1) bw.write(" ");
        }
        bw.write("\n");
        bw.close();
    }
}
