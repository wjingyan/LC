class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        carry = 0
        res = ''
        a = ''.join(reversed(a)) #reverse a string
        b = ''.join(reversed(b))
        # do not use function name for variable name such as len
        for i in range(0, max(len(a), len(b))): 
            v1 = int(a[i]) if i < len(a) else 0
            v2 = int(b[i]) if i < len(b) else 0
            sum = v1 + v2 + carry
            res += str(sum % 2)
            carry = sum / 2
        if carry != 0:
            res += str(carry)
        return ''.join(reversed(res))

        