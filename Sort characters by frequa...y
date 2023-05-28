from collections import Counter

class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        frequancy = Counter(s)
        sorted_chars = [char for char, count in frequancy.most_common()]
        result = ''
        for char in sorted_chars:
            result += char * frequancy[char]
        return result
