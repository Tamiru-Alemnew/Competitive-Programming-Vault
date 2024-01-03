class Solution(object):
    def isPalindrome(self, s):

        s = s.lower()
        arr = []
        for i in s:
            if i.isalnum():
                arr.append(i)

        left = 0
        right = len(arr) - 1

        while left < right:
            if arr[left] != arr[right]:
                return False
            left += 1
            right -= 1

        return True