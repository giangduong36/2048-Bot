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
    # 2048: 43,
    # 4096: 103,
    # 8192: 45,
    # 16384: 105,
    # 32768: 41,
    # 65536: 101,
}

class Grid:
    def __init__(self, size=4):
        self.size = size
        self.tile = [[2] * self.size for i in range(self.size)]

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

    def moveUpDown(self, down = False):
        r = range(self.size -1, -1, -1) if down else range(self.size)

        moved = False

        for j in range(self.size):
            cells = []

            for i in r:
                cell = self.tile[i][j]

                if cell != 0:
                    cells.append(cell)

            self.mergeTiles(cells)

            for i in r:
                value = cells.pop(0) if cells else 0

                if self.tile[i][j] != value:
                    moved = True

                self.tile[i][j] = value

        return moved

    def moveLeftRight(self, right=True):
        # if right:
        #     direction = (self.size - 1, -1, -1)
        # else:
        #     direction = range(self.size)
        # cells = []
        # for x in range(self.size):
        #     # temp = []
        #     for y in range(self.size):
        #         cells.append(self.tile[x][y])
        #     # cells.append(temp)
        #
        # cells =
        # self.mergeTiles(cells)
        # print(cells)
        # return

        r = range(self.size - 1, -1, -1) if right else range(self.size)

        moved = False

        for i in range(self.size):
            cells = []

            for j in r:
                cell = self.tile[i][j]

                if cell != 0:
                    cells.append(cell)

            self.mergeTiles(cells)

            for j in r:
                value = cells.pop(0) if cells else 0

                if self.tile[i][j] != value:
                    moved = True

                self.tile[i][j] = value

        return moved

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

    def canMove(self, direction):
        return

    def getAvailableMoves(self, direction):
        return

    def crossBound(self, pos):
        return

    def getCellValue(self):
        return

    def endGame(self):
        for x in range (self.size):
            for y in range (self.size):
                if self.tile[x][y] == 2048:
                    return True
        return False

if __name__ == '__main__':
    x = Grid()
    while not x.endGame():
        x.displayGrid()
        move = input('Enter move: ')
        if move == "l":
            x.moveLeftRight(False)
        elif move == "r":
            x.moveLeftRight(True)
        elif move == "u":
            x.moveUpDown(False)
        elif move == "d":
            x.moveUpDown(True)

