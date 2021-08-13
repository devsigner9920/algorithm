package me.devsign;

import java.io.*;
import java.util.Stack;

public class Main_17413 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        char[] text = br.readLine().toCharArray();
        Stack<Character> stack = new Stack<>();
        boolean tag = false;
        for(char c: text) {
            if(c == '<') {
                while(!stack.empty()) bw.write(stack.pop());
                bw.write(c);
                tag = true;
            } else if(c == '>') {
                bw.write(c);
                tag = false;
            } else if(tag) {
                bw.write(c);
            } else {
                if(c == ' ') {
                    while(!stack.empty()) bw.write(stack.pop());
                    bw.write(c);
                } else {
                    stack.add(c);
                }
            }
        }
        while(!stack.empty()) bw.write(stack.pop());
        bw.write('\n');
        bw.close();
    }
}
