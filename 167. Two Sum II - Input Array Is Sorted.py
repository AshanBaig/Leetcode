class Solution:
    def twoSum(self, numbers, target: int) :
        # for i in range(len(numbers)):
        #     for j in range(i+1,len(numbers)):
        #         if  numbers[i]+numbers[j]==target:
        #             return [min(i,j)+1,max(i,j)+1]
        i,j=0,len(numbers)-1
        while True:
            if numbers[i]+numbers[j]>target:
                j-=1
            elif numbers[i]+numbers[j]<target:
                i+=1
            elif numbers[i]+numbers[j]==target:
                return [i+1,j+1]
            


        