
class Solution:
    def maximumSwap(self, num: int) -> int:
        num = str(num)
        ans = list(num)
        position = [i for i in range(len(num))]

        for i in range(len(num) -2 , -1 , -1):
            if int(num[position[i]]) < int(num[i+1]):
                position[i] = i+1
            
            if int(num[position[i]]) <= int(num[position[i+1]]):
                position[i] = position[i+1]

        print(position)
        for i in range(len(num)):
            if int(num[i]) < int(num[position[i]]):

                ans[i] = num[position[i]]
                ans[position[i]] = num[i]
                break

        return int("".join(ans))

        