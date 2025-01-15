class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        if num1==num2: 
            return num1
        num2_b=bin(num2)[2:]
        num1_b=bin(num1)[2:]
        num2_b=(max(len(num2_b),len(num1_b))-len(num2_b))*"0"+num2_b
        num1_b=(max(len(num2_b),len(num1_b))-len(num1_b))*"0"+num1_b
        set_bit=num2_b.count("1")
        total=["0"]*len(num2_b)
        for i in range(len(num2_b)):
            if num1_b[i]=="1" and set_bit>0:
                set_bit-=1
                total[i]="1"
        put=-1
        while set_bit>0:
            # print(total,put,set_bit)
            if total[put]!="1":
                total[put]="1"
                set_bit-=1
            put-=1
        return int("".join(total),2)
        

        
