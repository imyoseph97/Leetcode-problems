class Solution():
    def reverse(self, x: int) -> int:
        positive_x = x
        if x < 0:
            positive_x *= -1

        n1  = str(positive_x)
        n2 = n1[::-1]

        f = int(n2)
        if -2**31 < f < 2**(31) -1:
            if x < 0:
                return f * -1
            else:
                return f
        else:
            return 0

        
         
        
solution = Solution()
print(solution.reverse(1534236469))