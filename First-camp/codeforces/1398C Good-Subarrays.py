t = int(input())

for _ in range(t):
    n = int(input())
    nums = input()
    p = {0: 1}
    c = 0
    r = 0
    for i, v in enumerate(nums):
        c += int(v)
        d = c - i - 1
        if d in p:
            r += p[d]
            p[d] += 1
        else:
            p[d] = 1
    print(r)
