class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        result = []
        
        a, b = a[::-1], b[::-1]  # Reverse the strings for easier processing
        
        # Iterate through both strings, adding digits and managing carry
        for i in range(max(len(a), len(b))):
            digit_a = int(a[i]) if i < len(a) else 0
            digit_b = int(b[i]) if i < len(b) else 0
            total = digit_a + digit_b + carry
            result.append(str(total % 2))
            carry = total // 2
        
        if carry:
            result.append(str(carry))
        
        return ''.join(result[::-1])  # Reverse the result to get the correct order
