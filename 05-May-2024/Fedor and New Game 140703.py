# Problem: Fedor and New Game - https://codeforces.com/contest/467/problem/B

n , m , k = map(int , input().split())
players = []
for i in range(m+1):
    players.append(int(input()))

fedor = players[-1]
ans = 0 

for soldier in players:
    current = soldier ^ fedor
    if current.bit_count() <= k:
        ans += 1

print(ans-1)

