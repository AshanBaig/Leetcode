class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        d={'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7,'i':8,'j':9,'k':10,'l':11,'m':12,'n':13,'o':14,'p':15,'q':16,'r':17,'s':18,'t':19,'u':20,'v':21,'w':22,'x':23,'y':24,'z':25}
        no_of_lines=1
        current_pixel=0
        for i in s:
            print(widths[d[i]])
            current_pixel+=widths[d[i]]
            if current_pixel<101:
                continue
            else:
                no_of_lines+=1
                current_pixel=widths[d[i]]
        return [no_of_lines,current_pixel]
        