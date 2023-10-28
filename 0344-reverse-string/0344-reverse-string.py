class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def recursive(ss, start, end):
            if start >= end:
                return ss

            ss[start], ss[end] = ss[end], ss[start]
            return recursive(s, start + 1, end - 1)
        return recursive(s, 0, len(s) - 1)
        