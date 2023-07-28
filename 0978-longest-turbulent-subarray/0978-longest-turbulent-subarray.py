class Solution:
    
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        
        left, right = 0, 1
        max_length, prev_comparison = 1, ""

        while right < len(arr):
            
            if arr[right - 1] > arr[right] and prev_comparison != ">":
                max_length = max(max_length, right - left + 1)
                right += 1
                prev_comparison = ">"
                
            elif arr[right - 1] < arr[right] and prev_comparison != "<":
                max_length = max(max_length, right - left + 1)
                right += 1
                prev_comparison = "<"
                
            else:
                right = right + 1 if arr[right - 1] == arr[right] else right
                left = right - 1
                prev_comparison = ""

        return max_length