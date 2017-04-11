colorMap = {
    0: "2;32;47",
    2: "1;33;41",
    4: "2;30;44",
    8: "1;34;42",
    16: "0;32;46",
    32: "1;33;45",
    64: 106,
    128: 44,
    256: 104,
    512: 42,
    1024: 102,
    2048: 43,
    4096: 103,
    # 8192: 45,
    # 16384: 105,
    # 32768: 41,
    # 65536: 101,
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

    def insertTile(self, pos, value):
        return

    def setTileValue(self, pos, value):
        return

    def getAvailableTiles(self):
        return

    def getMaxTile(self):
        return

    def isEmpty(self, pos):
        return

    def move(self, dir):
        return

    def moveUpDown(self, down):
        return

    def moveLeftRight(self, right):
        return

    def mergeTiles(self, cells):
        return

    def canMove(self, direction):
        return

    def getAvailableMoves(self, direction):
        return

    def crossBound(self, pos):
        return

    def getCellValue(self, pos):
        return

if __name__ == '__main__':
    x = Grid()
    x.displayGrid()
