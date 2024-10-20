class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        lst=[]
        def calculate(l,opr):
            if opr=="!":
                if l[0]=="f":
                    return "t"
                return "f"
            elif opr=="|":
                if "t" in l:
                    return  "t"
                return "f"        
            else:
                if  not ("f" in l):
                    return "t"
                return "f"
        for i in range(len(expression)):
            if expression[i]==")":
                item=lst.pop()
                l=[item]
                while item!="(":
                    item=lst.pop()
                    l.append(item)
                operator=lst.pop()
                lst.append(calculate(l,operator))
                
            else:
                if expression[i]!=",":
                    lst.append(expression[i])
        
        return lst[0]=="t"
