class Solution:
    def customSortString(self, order: str, s: str) -> str:
        order_hash = {char: i for i, char in enumerate(order)}
        return ''.join(sorted(s, key=lambda x: order_hash[x] if x in order else float('inf')))
