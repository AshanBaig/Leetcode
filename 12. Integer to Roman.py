class Solution:
    def intToRoman(self, num: int) -> str:
        d={1:'I',5:'V',10:'X',50:'L',100:'C',500:'D',1000:'M'}
        l=[1,5,10,50,100,500,1000]
        s=''
        while num:
            
           if str(num)[0]=='4' or str(num)[0]=='9':
            for i in range(len(l)-1):
                if l[i]<int(str(num)[0])<l[i+1]:
                    if int(str(num)[0])==9:
                        s+=d[l[i-1]*10**(len(str(num))-1)]
                    else:
                        s+=d[l[i]*10**(len(str(num))-1)]
                    s+=d[l[i+1]*10**(len(str(num))-1)]
                    num=str(num)[::-1][:len(str(num))-1][::-1]
                    if num=='':
                        return s
                    else:
                        num=int(num)
                    break
            continue
                    
           if num>999:
            s+='M'
            num-=1000
           elif num>499:
            s+='D'
            num-=500
           elif num>99:
            s+='C'
            num-=100
           elif num>49:
            s+="L"
            num-=50
           elif num>9:
            s+='X'
            num-=10
           elif num>4:
            s+='V'
            num-=5
           else:
            s+='I'
            num-=1
        return s
