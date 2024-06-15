#2037
class Solution:
    def minMovesToSeat(self, seats, students) -> int:
        seats.sort()
        students.sort()
        move=0
        for i in range(len(students)):
            move+=abs(students[i]-seats[i])
        return move

        