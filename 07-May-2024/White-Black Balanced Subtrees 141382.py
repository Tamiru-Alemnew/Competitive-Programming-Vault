# Problem: White-Black Balanced Subtrees - https://codeforces.com/contest/1676/problem/G

import sys, threading
 
input = lambda: sys.stdin.readline().strip()
 
def main():
    for _ in range(int(input())):
        n = int(input())
        arr = list(map(int, input().split()))
        graph = [ [] for _ in range(n)]
        colors = input()
 
        for i in range(len(arr)):
            graph[arr[i] - 1].append(i + 1)
        
        
        def dfs(idx):
            nonlocal ans
            
            white = colors[idx] == "W"
            black = colors[idx] == "B"
            for ed in graph[idx]:
                w, b = dfs(ed)
                white += w
                black += b
            
            if white == black:
                ans += 1
 
            return white, black
 
        ans = 0
        dfs(0)
        print(ans)
    
    pass
    
if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)
 
    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()