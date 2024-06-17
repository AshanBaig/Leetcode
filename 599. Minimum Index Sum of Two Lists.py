class Solution:
    def findRestaurant(self, list1, list2):
        l1=set(list1)
        l2=set(list2)
        mini=0
        inter=list(l1.intersection(l2))
        d={}
        for i in inter:
            d[i]=list1.index(i)+list2.index(i)
        mini=min(d.values())
        l=[]
        for i in d.keys():
            if d[i]==mini:
                l.append(i)
        return l
