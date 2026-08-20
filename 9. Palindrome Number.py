class Solution:
    def isPalindrome(self, x: int) -> bool:
        y = str(x)
        f  = y[::-1]
        if str(x) == f and -2**31 < x < 2**31 -1:
            return True
        else:
            return False

solution = Solution()
print(solution.isPalindrome(10))
