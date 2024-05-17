        for i in range(n):
            if is_palindrome[0][i]:
                min_cuts[i] = 0
            else:
                for j in range(i):
                    if is_palindrome[j + 1][i]:
                        min_cuts[i] = min(min_cuts[i], min_cuts[j] + 1)
 
        return min_cuts[-1]

"aab"
