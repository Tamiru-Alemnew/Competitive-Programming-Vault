import sys
input = sys.stdin.readline

def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
def invr():
    return(map(int,input().split()))

arr = insr()
test = "HQ9+"

for i in range(3):
    if test[i] in arr:
        print("YES")
        break
else:
    print("NO")
   