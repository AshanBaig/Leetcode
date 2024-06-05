#Leetcode258
class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while True:
            if len(str(num))==1:
                return num
            l=list(str(num))
            rvalue=0
            for i in l:
                rvalue+=int(i)
            num=rvalue
