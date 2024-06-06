class Solution:
    def isNStraightHand(self, hand,groupSize)-> bool:
        if len(hand)%groupSize==0:
            hand.sort()
            while True:
                if len(hand)==0:
                    return True
                n=hand[0]
                if len(hand)==0:
                    return True
                for i in range(groupSize):
                    if n+i in hand:
                        hand.remove(n+i)
                    else:
                        return False
        return False