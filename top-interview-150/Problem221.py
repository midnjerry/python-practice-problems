# https://leetcode.com/problems/maximal-square/?envType=study-plan-v2&envId=top-interview-150
class Problem221:
    def maximalSquare(self, matrix: list[list[str]]) -> int:
        height = len(matrix)
        width = len(matrix[0])

        maxSide = 0
        x = 0
        y = 0

        for y in range(height):
            for x in range(width):
                # To minimize scan times, only look for bigger squares, we start from top left corner and iterate
                # through every coordinate looking for a square that's bigger than current maxSide.
                # The idea is to fail fast.
                while (self.isBiggerSquare(x, y, maxSide, matrix, height, width)):
                    maxSide += 1
        return maxSide * maxSide

    def isBiggerSquare(self, startX: int, startY: int, currentSide: int, matrix: list[list[str]], height: int, width: int) -> bool:
        # if too close to right or bottom edge to beat current max, exit
        targetSide = currentSide + 1
        if (startX + targetSide > width or startY + targetSide > height):
            return False
        
        for y in range(startY, startY + targetSide):
            for x in range(startX, startX + targetSide):
                row = matrix[y]
                value = row[x]
                if (value == "0"):
                    return False
        return True


if __name__ == '__main__':
    solution = Problem221()
    matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
    area = solution.maximalSquare(matrix)
    print(f'Area (expected 4): {area}')
    print(f'Area (expected 1): {solution.maximalSquare([["0","1"],["1","0"]])}')