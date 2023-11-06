class Solution:
    def reverseStr(self, s: str, k: int) -> str:

        """
        Intuition: The problem asks us to reverse the first k characters for every 2k characters counting from the start of the string. This means that we need to process the string in chunks of 2k characters. If a chunk has less than k characters, we should reverse all of them. If a chunk has between k and 2k characters, we should reverse the first k characters and leave the others as original.

        Thought process: To solve the problem, we can iterate over the string in chunks of 2k characters. For each chunk, we can check if the chunk has less than k characters. If so, we should reverse all of the characters in the chunk. Otherwise, we should reverse the first k characters in the chunk and leave the others as original.

        Pseudo-code:
        for i in range(0, len(s), 2k):
            if i + k < len(s):
                reverse(s[i:i + k])
            else:
                reverse(s[i:])
        
        above Pseudo-code iterates over the string s in chunks of 2k characters. For each chunk, it checks if the chunk has less than k characters. If so, it reverses all of the characters in the chunk. Otherwise, it reverses the first k characters in the chunk and leaves the others as original.
        """
        # s=list(s)
        # for i in range(0, len(s), 2 * k):
        #     if i + k < len(s):
        #         s[i:i + k] = s[i:i + k][::-1]
        #     else:
        #         s[i:] = s[i:][::-1]
        
        # return "".join(s)


        """
        optimization on above

        """
        if k >= len(s):
            return s[::-1]
        
        i = 0
        s = list(s)
        while i < len(s):
            l = i
            h = (i + k - 1) if (i + k - 1) < len(s) else len(s) - 1
            while l < len(s) and l < h:
                s[l], s[h] = s[h], s[l]
                l += 1
                h -= 1
            i += (2 * k)
        return "".join(s)

