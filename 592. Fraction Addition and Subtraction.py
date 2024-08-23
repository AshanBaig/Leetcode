class Solution:
    def fractionAddition(self, expression: str) -> str:
        import re 
        import math 
        part_skip=re.split('([-+])',expression)
        skip=[]
        part=[]
        for p,s in enumerate(part_skip):
            if p%2==0:
                skip.append(s)
            else:
                part.append(s)
        if expression[0]=='-':
            part.pop(0)
            skip.pop(0)
            skip[0]='-'+skip[0]
        summ=skip[0]
        def find_lcm(n1,s,n2):
            if '/' not in n1:
                n1+='/1'
            if '/' not in n2:
                n2+='/1'
            if int(n1.split('/')[1])==int(n2.split('/')[1]):
                if s=='+':
                    temp=int(n1.split('/')[0])+int(n2.split('/')[0])
                else:
                    temp=int(n1.split('/')[0])-int(n2.split('/')[0])
                if temp/int(n2.split('/')[1])==int(temp/int(n2.split('/')[1])):
                    return str(int(temp/int(n2.split('/')[1])))+'/1'
                gcd=math.gcd(temp,int(n2.split('/')[1]))
                return str(int(temp/gcd))+'/'+str(int(int(n2.split('/')[1])/gcd))      
            else:
                lcm=abs(int(n2.split('/')[1])*int(n1.split('/')[1]))//math.gcd(int(n2.split('/')[1]),int(n1.split('/')[1]))
                if s=='+':
                    temp=int(lcm/int(n1.split('/')[1]))*int(n1.split('/')[0])+int(lcm/int(n2.split('/')[1])*int(n2.split('/')[0]))    
                else:

                    print('n1:',n1,int(lcm/int(n1.split('/')[1]))*int(n1.split('/')[0]))
                    temp=int(lcm/int(n1.split('/')[1]))*int(n1.split('/')[0])-int(lcm/int(n2.split('/')[1])*int(n2.split('/')[0]))    
                    print(temp)
            if temp/lcm==int(temp/lcm):
                return str(int(temp/lcm))+"/1"
            gcd=math.gcd(temp,lcm)
            return str(int(temp/gcd))+'/'+str(int(lcm/gcd))
        for i in range(1,len(skip)):
            summ=find_lcm(summ,part[i-1],skip[i])
        return summ