class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        prefix_sum = [0] * (len(s) + 1)
        
        # Calculate the prefix sum of shifts
        for left, right, direction in shifts:
            if direction:
                prefix_sum[left] += 1
                prefix_sum[right + 1] -= 1
            else:
                prefix_sum[left] -= 1
                prefix_sum[right + 1] += 1
        
        result = ""
        cumulative_shift = 0
        
        # Apply the shifts and construct the result string
        for i in range(len(s)):
            cumulative_shift += prefix_sum[i]
            shifted_value = (ord(s[i]) -ord('a')+ cumulative_shift) % 26
            shifted_char = chr( ord('a')+ shifted_value)
            result += shifted_char
        
        return result