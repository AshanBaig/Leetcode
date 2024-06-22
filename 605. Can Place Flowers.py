class Solution:
    def canPlaceFlowers(self, flowerbed, n: int) -> bool:
        for i in range(len(flowerbed)):
            if flowerbed[i]==0:
                if i-1==-1 or flowerbed[i-1]==0:
                    print(flowerbed,i,n,i+1<len(flowerbed))
                    if (i+1<len(flowerbed)) and flowerbed[i+1]==0:
                        flowerbed[i]=1
                        n-=1
                    elif i==len(flowerbed)-1:
                        n-=1       
        if n<=0:
            return True
        return False        



