package me.devsign;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.IOException;
import java.util.*;

public class Main_9012 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        Stack<Character> stack;

        int t = Integer.parseInt(br.readLine());

        while(t-- > 0) {
            stack = new Stack<>();
            char[] bracket = br.readLine().toCharArray();

            for(char bk: bracket) {
                if(stack.empty() && bk == ')') {
                    stack.add(bk);
                    break;
                }

                if(bk == '(') stack.add(bk);
                else stack.pop();
            }

            if(stack.empty()) bw.write("YES");
            else bw.write("NO");
            bw.write("\n");
            bw.flush();
        }
        bw.close();
    }
}
