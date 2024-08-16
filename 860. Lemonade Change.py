class Solution:
    def lemonadeChange(self, bills: list[int]) -> bool:
        total=0
        b=[]
        for i in bills:
            b.append(i)
            if i==10:
                try:
                    b.remove(5)
                except:
                    return False
            elif i==20:
                if 10 in b and 5 in b:
                    b.remove(10)
                    b.remove(5)
                elif b.count(5)>2:
                    for n in range(3):
                        b.remove(5)
                else:
                    return False
        return True            

        