package me.devsign;

import java.io.*;
import java.util.HashMap;
import java.util.Map;

public class Main_1003 {
    static Integer fibo[];
    static Map<Integer, Integer> map;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int t = Integer.parseInt(br.readLine());
        int x;
        for(int i = 0; i < t; ++i) {
            x = Integer.parseInt(br.readLine());
            map = new HashMap<>();
            map.put(0, 0);
            map.put(1, 0);
//            fibo = new Integer[x + 1];
//            fibo[0] = 0;
//            if(fibo.length > 1) fibo[1] = 1;
            fibonacci(x);
            bw.write(Integer.toString(map.get(0)) + " " + Integer.toString(map.get(1)));
            bw.flush();
        }
        bw.close();
    }

    static int fibonacci(int x) {
        if(x <= 1) {
            int add = map.get(x) + 1;
            map.put(x, add);
            return x;
        }
        return fibonacci(x - 1) + fibonacci(x - 2);

    }
}
