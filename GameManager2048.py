from Grid import *
from Decision import *
import time


class GameManager2048:
    """This is the main class to run the game. The user can choose either User mode and play themselves or AI mode"""

    def __init__(self, mode):
        if mode == "AI":
            self.mainAI()
        elif mode == "User":
            self.mainUser()

    def checkGameOver(self, grid):
        """Check if game is over"""
        return grid.loseGame()

    def mainUser(self):
        """Run User mode, read inputs from keyboard and allow the user to play 2048 themselves"""
        mainGrid = Grid()
        mainGrid.computerAddTile()
        mainGrid.displayGrid()
        while not mainGrid.loseGame():
            print("Player turn:")
            move = input('Enter move: ')
            if move == "l":
                mainGrid.moveLeftRight(False)
            elif move == "r":
                mainGrid.moveLeftRight(True)
            elif move == "u":
                mainGrid.moveUpDown(False)
            elif move == "d":
                mainGrid.moveUpDown(True)
            elif move == "q":
                break
            mainGrid.displayGrid()
            print("Computer turn:")
            mainGrid.computerAddTile()
            mainGrid.displayGrid()
        print("Max score: ", mainGrid.getMaxTile())

    def mainAI(self):
        """Run AI mode"""
        start = time.time()
        mainGrid = Grid()
        mainGrid.computerAddTile()
        aiPlayer = Decision()
        while not self.checkGameOver(mainGrid):
            print("\nCOMPUTER TURN:")
            mainGrid.computerAddTile()
            mainGrid.displayGrid()
            if not self.checkGameOver(mainGrid):
                move = aiPlayer.getMove(mainGrid)
                mainGrid.move(move)
                print("\nPLAYER TURN:")
                mainGrid.displayGrid()
        print("\nFINAL GRID:")
        mainGrid.displayGrid()
        end = time.time()
        scores = mainGrid.scores()
        print("Max score: ", mainGrid.getMaxTile())
        print("Total time: ", end - start)
        return scores, end - start

    def report(self, num):
        """A function to run the AI modes in num times and report on the success rate, average running time per game
        and the score distribution"""
        aveRunTime = 0
        successRate = 0
        scorePercent = {}
        for i in range(num):
            print("\tTurn: ", i + 1)
            result = self.mainAI()
            aveRunTime += result[1]
            maxVal = 0
            for val in result[0]:
                if val >= maxVal:
                    maxVal = val
            if maxVal >= 2048:
                successRate += 1
                if maxVal in scorePercent:
                    scorePercent[maxVal] += 1
                else:
                    scorePercent[maxVal] = 1
        return aveRunTime / num, successRate / num, scorePercent


if __name__ == '__main__':
    """Read input from the user and run either User or AI mode"""
    x = input("Enter either User mode or AI mode: ")
    if x == "User":
        game = GameManager2048("User")
    else:
        game = GameManager2048("AI")
