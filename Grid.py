from random import randint
from copy import deepcopy

# Assign colors for different values when printing the game in console
colorMap = {
    0: "4;32;47",
    2: "4;33;41",
    4: "4;33;44",
    8: "4;33;45",
    16: "4;33;44",
    32: "4;35;41",
    64: "4;34;42",
    128: "4;33;44",
    256: "4;33;41",
    512: "4;34;42",
    1024: "4;33;41",
    2048: "4;33;46",
    4096: "4;33;43",
    8192: "4;34;42",
}


class Grid:
    """This class represents a 4x4 grid of 2048 game"""

    def __init__(self, size=4):
        self.size = size
        self.tile = [[0] * self.size for i in range(self.size)]

    def gridSize(self):
        """Return the number of tiles per row in the grid"""
        return self.size

    def getTile(self, x, y):
        """Get a tile at a specific position"""
        return self.tile[x][y]

    def getTileByRow(self):
        """Get a list of all tiles in row order"""
        listTile = []
        for i in range(self.size):
            if i % 2 == 0:
                for j in range(self.size):
                    listTile.append(self.getTile(i, j))
            else:
                for j in range(self.size - 1, -1, -1):
                    listTile.append(self.getTile(i, j))
        return listTile

    def getTileByCol(self):
        """Get a list of all tiles in col order"""
        listTile = []
        for i in range(self.size):
            if i % 2 == 0:
                for j in range(self.size):
                    listTile.append(self.getTile(j, i))
            else:
                for j in range(self.size - 1, -1, -1):
                    listTile.append(self.getTile(j, i))
        return listTile

    def displayGrid(self):
        """Print the grid to console"""
        for i in range(self.size):
            for j in range(self.size):
                v = self.tile[i][j]
                print("\x1b[%sm %s \x1b[0m" % (colorMap[v], str(v).center(5, " ")), end=' ')
            print(" ")
            if i % 4 != -1:
                print("")

    def setTileValue(self, pos, value):
        """Set a tile to a value"""
        self.tile[pos[0]][pos[1]] = value

    def getAvailableTiles(self):
        """Get positions of empty tiles in the grid"""
        emptyPos = []
        for x in range(self.size):
            for y in range(self.size):
                if self.tile[x][y] == 0:
                    emptyPos.append([x, y])
        return emptyPos

    def getMaxTile(self):
        """Get the maximum value of tiles in the grid"""
        maxTile = 0
        for x in range(self.size):
            for y in range(self.size):
                if self.getTile(x, y) > maxTile:
                    maxTile = self.getTile(x, y)
        return maxTile

    def cloneGrid(self):
        """Clone the grid to work on a copy"""
        clone = Grid()
        clone.size = self.size
        clone.tile = deepcopy(self.tile)
        return clone

    def move(self, dir):
        """Move the grid in a direction
        Direction 1 is the Right direction, 
        Direction -1 is the Left direction, 
        Direction 10 is the Up direction, 
        Direction -10 is the Down direction, 
        """
        if dir == 1:
            self.moveLeftRight(True)
        elif dir == -1:
            self.moveLeftRight(False)
        elif dir == 10:
            self.moveUpDown(False)
        elif dir == -10:
            self.moveUpDown(True)

    def moveUpDown(self, down=False):
        """Move the grid up or down and merge tiles"""
        if down:
            r = range(self.size - 1, -1, -1)
        else:
            r = range(self.size)
        for j in range(self.size):
            tiles = []
            for i in r:
                tile = self.tile[i][j]
                if tile != 0:
                    tiles.append(tile)
            tiles = self.mergeTiles(tiles)
            if len(tiles) >= 0:
                k = 0
                for i in r:
                    if k < len(tiles):
                        self.tile[i][j] = tiles[k]
                        k += 1
                    else:
                        self.tile[i][j] = 0
        return

    def moveLeftRight(self, right=True):
        """Move the grid left or right and merge tiles"""
        if right:
            r = range(self.size - 1, -1, -1)
        else:
            r = range(self.size)

        for i in range(self.size):
            tiles = []
            for j in r:
                tile = self.tile[i][j]
                if tile != 0:
                    tiles.append(tile)
            tiles = self.mergeTiles(tiles)
            if len(tiles) >= 0:
                k = 0
                for j in r:
                    if k < len(tiles):
                        self.tile[i][j] = tiles[k]
                        k += 1
                    else:
                        self.tile[i][j] = 0
        return

    def mergeTiles(self, tiles):
        """Merge a list of tiles. If two adjacent tiles are equal in values, they are merged together"""
        if len(tiles) <= 1:
            return tiles
        i = 0
        while i < len(tiles) - 1:
            if tiles[i] == tiles[i + 1]:
                tiles[i] *= 2
                del tiles[i + 1]
            i += 1
        return tiles

    def canMove(self, direction):
        """Check if there is any move left for the grid"""
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
        """Get all the available moves for the grid"""
        moveList = []
        for dir in (1, -1, 10, -10):
            if self.canMove(dir):
                moveList.append(dir)
        return moveList

    def wonGame(self):
        """Check if AI/User has won the game by getting a tile >= 2048"""
        if self.getMaxTile() >= 2048:
            return True

    def loseGame(self):
        """Check if AI/User has lost the game"""
        if len(self.getAvailableMoves()) == 0:
            return True

    def scores(self):
        """Return the score distribution of a grid in a sorted order"""
        scoreList = {}
        for x in range(self.size):
            for y in range(self.size):
                val = self.getTile(x, y)
                if val in scoreList:
                    scoreList[val] += 1
                else:
                    scoreList[val] = 1
        sortList = sorted(scoreList)
        scoreListFinal = {}
        for val in sortList:
            scoreListFinal[val] = scoreList[val]
        return scoreListFinal

    def computerAddTile(self):
        """Computer adds 2 90% of the time, add 4 10% of the time"""
        available = self.getAvailableTiles()
        i = randint(0, len(available) - 1)
        val = randint(1, 10) < 9 and 2 or 4
        self.setTileValue(available[i], val)
