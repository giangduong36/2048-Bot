from random import randint
import math


class Decision:
    def evaluate(self, grid):
        weight = [[17, 9, 5, 3], [8, 4, 2, 0], [3, 1, 0, 0], [0, 0, 0, 0]]
        # count = 17 * grid.tile[0][0] + 9 * grid.tile[0][1] + 5 * grid.tile[0][2] + 3 * grid.tile[0][3]
        # count += 8 * grid.tile[1][0] + 4 * grid.tile[1][1] + 2 * grid.tile[1][2]
        # count += 3 * grid.tile[2][0] + 1 * grid.tile[2][1]
        count = 0
        for i in range(grid.size):
            for j in range(grid.size):
                count += grid.tile[i][j] * grid.tile[i][j] * weight[i][j]
        # return count
        return count*11 + len(grid.getAvailableTiles())*5 + self.monotonicity(grid) * 7

        # count = 0
        # for i in range(grid.size - 1):
        #     for j in range(grid.size-1):
        #         count+= grid.tile[i][j]
        # return count
        # return grid.getMaxTile()

    def penalty(self, grid):
        penalty = 0
        for i in range(grid.size):
            for j in range(grid.size):
                current = grid.getTile(i, j)
                for n in grid.getNeighbors(i, j):
                    penalty += abs(current - grid.getTile(n[0], n[1]))
        return penalty

    def monotonicity(self,grid):
        penalty = 0
        for i in range(grid.size):
            currentList = []
            for j in range(grid.size):
                currentList.append(grid.getTile(i, j))
            if not self.checkMonotone(currentList):
                return False
        return True

    def checkMonotone(self, aList):
        dir = aList[1] - aList[0]
        for i in range(2,len(aList)):
            if (aList[i] - aList[i-1])*dir < 0:
                return False
        return True

    def getMove(self, state):
        if len(state.getAvailableTiles()) < 5:
            move = self.maximize(state, 0, - math.inf, math.inf, 6)[0]
        else:
            move = self.maximize(state, 0, - math.inf, math.inf, 6)[0]
        # return best move found
        moves = state.getAvailableMoves()
        if move in moves:
            return move
        return moves[randint(0, len(moves) - 1)]

    def minimize(self, state, maxMove, alpha, beta, depth):
        statecloneGrid = state.cloneGrid()
        minMove = None
        minUtil = math.inf
        for pos in state.getAvailableTiles():
            statecloneGrid.setTileValue(pos, 2)
            tempUtil = self.maximize(statecloneGrid, maxMove, alpha, beta, depth - 1)
            statecloneGrid.setTileValue(pos, 0)
            if tempUtil[1] < minUtil:
                minMove = tempUtil[0]
                minUtil = tempUtil[1]
            if minUtil <= alpha:
                break
            if minUtil < beta:
                beta = minUtil

        # for pos in state.getAvailableTiles():
        #     statecloneGrid.setTileValue(pos, 4)
        #     tempUtil = self.maximize(statecloneGrid, maxMove, alpha, beta, depth - 1)
        #     statecloneGrid.setTileValue(pos, 0)
        #     if tempUtil[1] < minUtil:
        #         minMove = tempUtil[0]
        #         minUtil = tempUtil[1]
        #     if minUtil <= alpha:
        #         break
        #     if minUtil < beta:
        #         beta = minUtil

        return minMove, minUtil

    def maximize(self, state, minMove, alpha, beta, depth):
        if depth == 0:
            return minMove, self.evaluate(state)

        maxMove = None
        maxUtil = -math.inf

        for move in state.getAvailableMoves():
            statecloneGrid = state.cloneGrid()
            statecloneGrid.move(move)
            tempUtil = self.minimize(statecloneGrid, move, alpha, beta, depth - 1)[1]
            if tempUtil > maxUtil:
                maxMove = move
                maxUtil = tempUtil
            if maxUtil >= beta:
                break
            if maxUtil > alpha:
                alpha = maxUtil
        return maxMove, maxUtil

if __name__ == '__main__':
    x = Decision()
    aList = [2,1,0,10]
    print(x.checkMonotone(aList))