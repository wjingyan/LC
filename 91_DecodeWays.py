class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0 or int(s[0:1]) == 0: 
            return 0
        if len(s) == 1:
            return 1
        res = [1]
        res.append(0 if int(s[1:2]) == 0 else 1)
        for i in range(2, len(s) + 1):
            num2 = int(s[i - 2: i])
            num1 = int(s[i - 1: i]) #10
            if num2 == 0 or (num1 == 0 and num2 > 26): #720
                return 0
            elif num1 == 0:
                res.append(res[i - 2])
            elif num2 <= 26 and num1 != num2: #7206
                res.append(res[i - 1] + res[i - 2])
            else:
                res.append(res[i - 1])
        return res[len(s)]
        
