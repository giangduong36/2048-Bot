from Grid import *
from Decision import *


class MainGame:
    def checkGameOver(self, grid):
        return grid.loseGame()

    def mode(self, mode):
        pass

    def main(self):
        start = time.time()
        mainGrid = Grid()
        mainGrid.computerAddTile()
        aiPlayer = Decision()
        while not self.checkGameOver(mainGrid):
            # print("\nCOMPUTER TURN:")
            mainGrid.computerAddTile()
            # mainGrid.displayGrid()
            if not self.checkGameOver(mainGrid):
                move = aiPlayer.getMove(mainGrid)
                mainGrid.move(move)
                # print("\nPLAYER TURN:")
                # mainGrid.displayGrid()
                # print(mainGrid.getMaxTile())
        # mainGrid.displayGrid()
        end = time.time()
        scores = mainGrid.scores()
        print("\t\t", mainGrid.getMaxTile())
        # print("Time: ", end - start)
        return scores, end - start

    def report(self, num):
        aveRunTime = 0
        successRate = 0
        scorePercent = {}
        for i in range(num):
            print("\tTurn: ", i)
            result = self.main()
            aveRunTime += result[1]
            if result[1].getMaxTile() >= 2048:
                successRate += 1
            for val in result[0]:
                if val in scorePercent:
                    scorePercent[val] += 1
                else:
                    scorePercent[val] = 1
        return aveRunTime / num, successRate / num, scorePercent


if __name__ == '__main__':
    game = MainGame()
    # game.main()
    for i in range(5):
        print("Report: ", i)
        print(game.report(10))
