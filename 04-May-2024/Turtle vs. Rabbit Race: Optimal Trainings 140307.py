# Problem: Turtle vs. Rabbit Race: Optimal Trainings - https://codeforces.com/contest/1933/problem/E

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int , input().split()))
    ps = [0]

    for a in arr:
        ps.append(ps[-1] + a)

    ans = []
    for i in range(int(input())):
        l, u = map(int, input().split())
        left = l-1
        r = n

        while l < r:
            mid = (l+r + 1) // 2

            if ps[mid] <= u+ps[left]:
                l = mid 
            else:
                r = mid - 1 

        if l + 1 < n + 1 and abs(ps[l] - (u + ps[left])) > abs(ps[l + 1] - (u+ps[left]))-1:
            l += 1

        ans.append(l)
    
    print(*ans)




