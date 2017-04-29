import random
from copy import deepcopy
from Decision import *

colorMap = {
    0: "2;32;47",
    2: "1;33;41",
    4: "2;30;44",
    8: "1;34;42",
    16: "0;32;46",
    32: "1;33;45",
    64: "1;31;46",
    128: "2;30;44",
    256: "0;32;46",
    512: "1;34;42",
    1024: "1;33;41",
    2048: "0;32;46",
    # 4096: ,
    # 8192: ,
}


class Grid:
    def __init__(self, size=4):
        self.size = size
        self.tile = [[0] * self.size for i in range(self.size)]

    def gridSize(self):
        return self.size

    def getTile(self, x, y):
        return self.tile[x][y]

    def displayGrid(self):
        for i in range(self.size):
            for j in range(self.size):
                v = self.tile[i][j]
                print("\x1b[%sm %s \x1b[0m" % (colorMap[v], str(v).center(5, " ")), end=' ')
            print(" ")
            if i % 4 != -1:
                print("")

    # Insert new tile at a position
    def insertTile(self, pos, value):
        self.tile[pos[0]][pos[1]] = value

    def setTileValue(self, pos, value):
        self.tile[pos[0]][pos[1]] = value

    def getAvailableTiles(self):
        emptyPos = []
        for x in range(self.size):
            for y in range(self.size):
                if self.tile[x][y] == 0:
                    emptyPos.append([x, y])
        return emptyPos

    def getMaxTile(self):
        maxTile = 0
        for x in range(self.size):
            for y in range(self.size):
                if self.getTile(x, y) > maxTile:
                    maxTile = self.getTile(x, y)
        return maxTile

    def cloneGrid(self):
        clone = Grid()
        clone.size = self.size
        clone.tile = deepcopy(self.tile)
        return clone

    def isEmpty(self, pos):
        return self.tile[pos[0]][pos[1]] == 0

    def move(self, dir):
        return

    def moveUpDown(self, down=False):
        if down:
            r = range(self.size - 1, -1, -1)
        else:
            r = range(self.size)
        for j in range(self.size):
            cells = []
            for i in r:
                cell = self.tile[i][j]
                if cell != 0:
                    cells.append(cell)
            self.mergeTiles(cells)
            for i in r:
                if cells:
                    value = cells.pop(0)
                else:
                    value = 0
                self.tile[i][j] = value

        return

    def moveLeftRight(self, right=True):
        if right:
            r = range(self.size - 1, -1, -1)
        else:
            r = range(self.size)

        for i in range(self.size):
            cells = []
            for j in r:
                cell = self.tile[i][j]
                if cell != 0:
                    cells.append(cell)
            self.mergeTiles(cells)
            for j in r:
                if cells:
                    value = cells.pop(0)
                else:
                    value = 0
                self.tile[i][j] = value

        return

    def mergeTiles(self, cells):
        if len(cells) <= 1:
            return cells
        i = 0
        while i < len(cells) - 1:
            if cells[i] == cells[i + 1]:
                cells[i] *= 2
                del cells[i + 1]
            i += 1
        return cells

    #
    def canMove(self, direction):
        clone = self.cloneGrid()
        if direction == 1:
            clone.moveLeftRight(True)
        elif direction == -1:
            clone.moveLeftRight(False)
        elif direction == 10:
            clone.moveUpDown(False)
        else:
            clone.moveUpDown(True)
        if clone.tile == self.tile:
            return False
        else:
            return True

    def getAvailableMoves(self):
        moveList = []
        for dir in (1,-1,10,-10):
            if self.canMove(dir):
                moveList.append(dir)
        return moveList

    def wonGame(self):
        for x in range(self.size):
            for y in range(self.size):
                if self.tile[x][y] >= 2048:
                    return True

    def loseGame(self):
        if len(self.getAvailableMoves()) == 0:
            return True

    # def run(self):
    #     available = self.getAvailableTiles()
    #     print(available)
    #     i = random.randint(0, len(available) - 1)
    #     self.insertTile(available[i], random.randint(1, 2) * 2)
    #     self.displayGrid()


if __name__ == '__main__':
    x = Grid()
    ai = Decision()
    available = x.getAvailableTiles()
    i = random.randint(0, len(available) - 1)
    # x.insertTile(available[i], random.randint(1, 2) * 2)
    x.insertTile(available[i], 2)
    while not (x.wonGame() or x.loseGame()):
        available = x.getAvailableTiles()
        i = random.randint(0, len(available) - 1)
        # x.insertTile(available[i], random.randint(1, 2) * 2)
        x.insertTile(available[i], 2)
        while not (x.loseGame()):
            x.displayGrid()
            print(x.getAvailableMoves())
            move = ai.getNextMove(x)
        # move = input('Enter move: ')
        #
        # if move == "l":
        #     x.moveLeftRight(False)
        # elif move == "r":
        #     x.moveLeftRight(True)
        # elif move == "u":
        #     x.moveUpDown(False)
        # elif move == "d":
        #     x.moveUpDown(True)
        # else:
        #     break
            if move == -1:
                x.moveLeftRight(False)
            elif move == 1:
                x.moveLeftRight(True)
            elif move == 10:
                x.moveUpDown(False)
            elif move == -10:
                x.moveUpDown(True)
            break
    x.displayGrid()
    #
    # dic = [1,2,3,4]
    # for i in dic:
    #     print(i)
