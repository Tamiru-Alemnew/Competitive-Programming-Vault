# Problem: Array Manipulation - https://www.hackerrank.com/challenges/crush/problem

def arrayManipulation(n, queries):
    pref_sum=[0 for i in range(n+1)]
    
    for query in queries:
        i, j, k= query[o], query[1], query[2]
        pref_sum[i-1]+=k
        pref[j]-=k
        
    for  i in range(1,n+1):
        pref_sum[i]+=pref_sum[i-1]
        
    return max(pref_sum)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
