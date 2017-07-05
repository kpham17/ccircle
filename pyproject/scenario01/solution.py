
import worlds
# Your solution goes in this file!

'''
    GOAL: Fill in the code for 'moveTowardPizza' to ensure that the cat finds the pizza!

    Use the following functions to understand the cat's situation:

        cat.isBlocked() -> Bool
            returns True if the cat is facing a wall or the edge of the maze, False if the coast is clear
        cat.isFacingN() -> Bool
            True iff cat is facing north
        cat.isFacingS() -> Bool
            True iff cat is facing south
        cat.isFacingE() -> Bool
            True iff cat is facing east
        cat.isFacingW() -> Bool
            True iff cat is facing west
        cat.smellsPizza() -> Bool
            True iff the cat is right in front of the pizza (and is facing it)

        Just a refresher...:

                   /|\
                    |
                  North
                    |
        <-- West --- --- East --->
                    |
                    |
                  South
                    |
                   \|/

    Use the following functions to instruct the cat:

        cat.turnLeft() -> None
            Instructs the cat to turn left / counter-clockwise
        cat.turnRight() -> None
            Instructs the cat to turn right / clockwise
        cat.walk() -> None
            Instructs the cat to walk in the direction it is facing

    NOTE: You can only call cat.walk() ONCE per call to moveTowardPizza!!
'''

class Solution:
    def __init__(self):
        self.blockedRight = False
        self.justWalked = False
        self.checked = False
        pass

    # Choose your level here: 'worlds.easy()', 'worlds.medium()', or 'worlds.hard()'!
    def getLevel(self):
        return worlds.hard()

    # Smaller pause time = faster simulation
    def getPauseTime(self):
        return 0.2

    # Your solution!
    def moveTowardPizza(self, cat):
        if (self.blockedRight and not cat.isBlocked()) or (self.checked and not cat.isBlocked()):
            cat.walk()
            self.justWalked = True
            self.blockedRight = False
            self.checked = False
        elif self.justWalked:
            cat.turnRight()
            self.justWalked = False
            self.checked = True
        else:
        cat.turnLeft()self.blockedRight = True