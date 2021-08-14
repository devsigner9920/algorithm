package me.devsign;

import java.io.*;

public class Main_1463 {
    private static int[] d;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = Integer.parseInt(br.readLine());
        d = new int[n + 1];
        for(int i = 0; i < n + 1; ++i) d[i] = 0;
        //System.out.println("n = " + go(n));
        //System.out.println("n = " + Arrays.toString(d));
        bw.write(go(n) + "\n");
        bw.close();
    }

    public static int go(int n) {
        if(n == 1) return 0;
        if(d[n] > 0) return d[n];
        d[n] = go(n - 1) + 1;
        if(n % 2 == 0) {
            int tmp = go(n / 2) + 1;
            if(d[n] > tmp) d[n] = tmp;
        } else if(n % 3 == 0) {
            int tmp = go(n / 3) + 1;
            if(d[n] > tmp) d[n] = tmp;
        }

        return d[n];
    }
}
