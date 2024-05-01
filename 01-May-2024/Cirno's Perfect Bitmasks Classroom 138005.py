# Problem: Cirno's Perfect Bitmasks Classroom - https://codeforces.com/problemset/problem/1688/A

n = int(input())

for i in range(n):
    num = int(input())
    cur = num
    cnt = 0 
    ans = 0 
    if cur == 1:
        print(3)
        continue
    
    while cur > 0:
        if cur & 1:
            ans += 2**cnt
            break
        cnt += 1
        cur >>=1

    if ans == num:
        ans += 1

    print(ans)









