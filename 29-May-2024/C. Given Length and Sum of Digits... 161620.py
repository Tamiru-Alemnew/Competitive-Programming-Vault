# Problem: C. Given Length and Sum of Digits... - https://codeforces.com/contest/489/problem/C

m, n = map(int, input().split())
max_val = 0
min_val = float("inf")
def cann(sm , ln ):
    return 0 <= sm <= 9 * ln

def bt(path, cur_sum, length , i , j , s):
    if cur_sum > n or length > m or not cann(n - cur_sum , m - length):
        return
    if cur_sum == n and length == m:
        return "".join(path)

    for i in range(i, j , s):
        path.append(str(i))
        cur = bt(path, cur_sum + i, length + 1 , i , j , s)
        if cur :
            return cur
        
        path.pop()


if 0 < n <= 9 * m:
    for i in range(1, 10):
       cur = bt([str(i)], i, 1 , 0 , 10 , 1)
       if  cur:
           min_val = cur
           break

    max_val = bt([], 0, 0 , 9 , -1, -1)
    print(min_val, max_val)
    
elif n == 0 and m == 1:
    print("0"*m ,"0"*m)

else:
    print(-1, -1)
