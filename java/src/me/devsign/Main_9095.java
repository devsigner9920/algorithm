package me.devsign;

import java.io.*;

public class Main_9095 {
    static Integer dp[];
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int t = Integer.parseInt(br.readLine());
        int x;
        for(int i = 0; i < t; ++i) {
            x = Integer.parseInt(br.readLine());
            dp = new Integer[x + 1];
            dp[0] = dp[1] = 1;
            System.out.println(count(x));
        }
    }

    static int count(int x) {
        if (x == 1 || x == 0) return 1;
        int cnt = 0;

        for (int i = 1; i <= 3; ++i) {
            if(x - i >= 0) {
                if(dp[x - i] == null)
                    dp[x - i] = count(x - i);
                cnt += dp[x - i];
            }
        }

        return cnt;
    }
}
