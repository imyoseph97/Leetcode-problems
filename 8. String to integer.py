class Solution:
    def myAtoi(self, s: str) -> int:

        n = ["0","1","2","3","4","5","6","7","8","9"]
        n_list = []
        sign = 1
        for index, l in enumerate(s):
            if l.isalpha() or l == ".":
                if not n_list:
                    return 0
                else:
                    break
            elif l == " " and (len(s) != 1):
                if s[index - 1] in n and index != 0: 
                    break
                else:
                    continue
            elif l == "0" and (len(s) != 1) and(index != len(s)-1) :
                if s[index + 1] in n[1:] and s[index - 1] not in n:
                    continue
                else:
                    n_list.append(l)
            
            elif (l == "-"  or l == "+" ) and len(s) != 1:
                if index != len(s) -1 and s[index +1] in n:                               
                    if (s[index - 1] == " "and index != 0) or index == 0:
                        if l == "-":
                            sign = -1
                        else:
                            sign = 1
                    else:
                        break
                elif s[index - 1] in n and index != 0 or (index != len(s)-1 and s[index + 1] == ' '):
                    break
            elif l in n:
                n_list.append(l)
            else:
                return 0
        number = 0
        
        for n in n_list:
            number = number * 10 + int(n) 
        
        final = number * sign
        if final >= 2**(31) -1:
            final = 2**(31) -1
        elif final < -2**31:
            final = -2**31
        
        return final



solution = Solution()
print(solution.myAtoi(" -1010023630o4"))

