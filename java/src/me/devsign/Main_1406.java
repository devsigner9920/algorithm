package me.devsign;

import java.io.*;
import java.util.Stack;

public class Main_1406 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        Stack<Character> stack1 = new Stack<>();
        Stack<Character> stack2 = new Stack<>();

        for(char c: br.readLine().toCharArray()) stack1.add(c);
        int n = Integer.parseInt(br.readLine());
        for(int i = 0; i < n; ++i) {
            String[] in = br.readLine().split(" ");
            if(in[0].equals("L")) {
                if(!stack1.empty()) stack2.add(stack1.pop());
            } else if(in[0].equals("D")) {
                if(!stack2.empty()) stack1.add(stack2.pop());
            } else if(in[0].equals("B")) {
                if(!stack1.empty()) stack1.pop();
            } else if(in[0].equals("P")) {
                stack1.add(in[1].toCharArray()[0]);
            }
        }
        while(!stack2.empty()) stack1.add(stack2.pop());

        for(Object c: stack1.toArray()) {
            bw.write((char) c);
        }
        bw.write("\n");
        bw.close();
    }
}
