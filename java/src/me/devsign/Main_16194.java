package me.devsign;

import java.io.*;

public class Main_16194 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = Integer.parseInt(br.readLine());
        Integer[] p = new Integer[n + 1];
        Integer[] dp = new Integer[n + 1];
        p[0] = 10001;
        dp[0] = 10001;
        int i = 1;
        for(String a: br.readLine().split(" ")) p[i++] = Integer.parseInt(a);

        for(i = 1; i < n + 1; i++) {
            dp[i] = p[i];
            for(int j = 1; j <= i; j++) {
                dp[i] = Math.min(dp[i], dp[i - j] + p[j]);
            }
        }

        bw.write(dp[dp.length - 1] + "\n");

        bw.close();
    }
}
