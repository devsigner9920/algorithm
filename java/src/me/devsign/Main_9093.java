package me.devsign;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.IOException;
import java.util.*;

public class Main_9093 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        Stack<Character> stack = new Stack<>();
        
        int t = Integer.parseInt(br.readLine());

        while(t-- > 0) {
            char[] line = (br.readLine() + "\n").toCharArray();

            for(char arg: line) {
                if(arg == ' ' || arg == '\n') {
                    while(!stack.isEmpty()) bw.write(stack.pop());
                    bw.write(arg);
                } else {
                    stack.add(arg);
                }
            }
            bw.flush();
        }

        bw.close();
    }
}
