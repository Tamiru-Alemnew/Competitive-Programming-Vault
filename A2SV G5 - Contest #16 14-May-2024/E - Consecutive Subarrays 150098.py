# Problem: E - Consecutive Subarrays - https://codeforces.com/gym/523525/problem/E


n , k = map(int , input().split())
arr = list(map(int , input().split()))

suffix = [0]*n
suffix[-1] = arr[-1]

max_k = []
for i in range(n-2 , -1 , -1):
    suffix[i] += suffix[i + 1] + arr[i]


ans = suffix[0]
suffix = sorted(suffix[1:] ,reverse=True)
ans += sum(suffix[:k-1])
print(ans)


