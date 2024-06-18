class Solution:
    def maxProfitAssignment(self, difficulty, profit, worker) -> int:
        total=0
        jobs = sorted(zip(profit, difficulty),reverse=True)
        #print(jobs)
        for i in worker:
            for p,d in jobs:
                if d<=i:
                    total+=p

                    break
        return total