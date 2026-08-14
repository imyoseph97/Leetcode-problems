class Solution:
    def longestPalindrome(self, s: str) -> str:
        words = []
        pwords = []
        x = len(s)
        for l in range(len(s)):
            
            for i in range(l, x):
                if i == 0:
                    words.append(s[i])
                    continue
                else:
                    words.append(s[i])
                    if words == words[::-1] and len(words) != 1:
                        pwords.append(words.copy())
            words.clear()
            
    
        pword = max(pwords, key=len)
        word = "".join(pword)
        return word
solution = Solution()
print(solution.longestPalindrome("cbbggfffffffffdgfgfgd"))                 
            