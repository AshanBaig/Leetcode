class Solution:
    def twoSum(self, numbers, target: int) :
        i,j=0,len(numbers)-1
        while True:
            if numbers[i]+numbers[j]>target:
                j-=1
            elif numbers[i]+numbers[j]<target:
                i+=1
            elif numbers[i]+numbers[j]==target:
                return [i+1,j+1]
            


        