package me.devsign;

import java.io.*;
import java.util.Arrays;

public class Main_daijkstra_simple {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String[] inp = br.readLine().split(" ");

        // 노드의 개수
        int n = Integer.parseInt(inp[0]);
        // 간선의 개수
        int m = Integer.parseInt(inp[1]);
        // 시작 노드 번호
        int start = Integer.parseInt(br.readLine());

        // 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트 만들기 (2차원배열)
        int[][] graph = new int[n + 1][0];

        // 방문한 노드인지 체크 리스트
        boolean[] visited = new boolean[n + 1];
        // 최단 거리 테이블 리스트
        long[] distance = new long[n + 1];
        for(int i = 0; i <= n; ++i) {
            // 방문 여부 리스트 초기화
            visited[i] = false;
            // 최단 거리 테이블 리스트 Long Max value 로 초기화
            distance[i] = Long.MAX_VALUE;
        }

        // 모든 간선 정보를 입력받기
        for(int i = 0; i < m; ++i) {
            int[] line_info = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();

            // a번 노드에서 b번 노드로 가는 비용이 c라는 의미
            int a = line_info[0];
            int b = line_info[1];
            int c = line_info[2];
            
            graph[a] = addElement(graph[a], b);
            graph[a] = addElement(graph[a], c);
        }

        System.out.println("Arrays.toString(graph) = " + Arrays.toString(graph[5]));

        bw.close();
    }

    static int[] addElement(int[] a, int e) {
        a  = Arrays.copyOf(a, a.length + 1);
        a[a.length - 1] = e;
        return a;
    }
}
