class Solution:
    def append_s(self,n):
        self.s+=self.d[n]
        self.num-=n
    def intToRoman(self, num: int) -> str:
        self.s=''
        self.num=num
        self.d={1000:'M',900:'CM',500: "D",400: "CD",100: "C",90: "XC",50:'L',40: "XL",10:'X',9:'IX',5:'V',4:'IV',1:'I'}
        while self.num:
            for i in self.d:
                if self.num>=i:
                    self.append_s(i)
                    break
        return self.s

