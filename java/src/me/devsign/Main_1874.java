package me.devsign;

import java.io.*;
import java.util.Stack;

public class Main_1874 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = Integer.parseInt(br.readLine());
        Stack<Integer> stack = new Stack<>();
        int count = 1;
        StringBuilder sb = new StringBuilder();
        for(int i = 0; i < n; ++i) {
            int in = Integer.parseInt(br.readLine());
            if(count <= in) {
                while(count <= in) {
                    stack.add(count++);
                    sb.append("+\n");
                }
                stack.pop();
                sb.append("-\n");
            } else {
                boolean found = false;
                if(!stack.isEmpty()) {
                    int top = stack.pop();
                    sb.append("-\n");
                    if(top == in) {
                        found = true;
                    }
                }

                if(!found) {
                    sb = new StringBuilder("NO\n");
                    break;
                }
            }
        }

        for(char c :sb.toString().toCharArray()) {
            bw.write(c);
        }
        bw.close();
    }
}
