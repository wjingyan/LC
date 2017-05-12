class Solution(object):
    # Recursion
    def letterCombinations1(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) == 0:
            return []
        return self.helper(digits)
        
    def helper(self, digits):
        if len(digits) == 0:
            return [""]
        dict = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        list = []
        letterList = dict[digits[-1:]]
        for c in letterList:
            for prevLetters in self.helper(digits[:-1]):
                    list.append(prevLetters + c)
        return list

    # Iteration
    def letterCombinations2(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) == 0:
            return []
        dict = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        list = []
        letterList = dict[digits[-1:]]
        for c in letterList:
            if len(digits) > 1:
                for prevLetters in self.letterCombinations(digits[:-1]):
                    list.append(prevLetters + c)
            else:
                list.append(c)
        return list
    
    # Another iteration that's faster
    def letterCombinations3(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        dict = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        list = []
        for c in digits:
            code = dict[c]
            nextList = []
            for c2 in code:
                if len(list) == 0:
                    nextList.append(c2)
                else:
                    for prevCode in list:
                        nextList.append(prevCode + c2)
            list = nextList
        return list