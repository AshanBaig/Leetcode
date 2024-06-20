class Solution:
    def judgeCircle(self, moves: str) -> bool:
        if (moves.count('U')!=moves.count('D')) or  (moves.count('R')!=moves.count('L')):
            return False
        return True
        