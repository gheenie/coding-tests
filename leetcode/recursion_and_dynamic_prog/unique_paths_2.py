from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        total_rows = len(obstacleGrid)
        total_columns = len(obstacleGrid[0])
        # Variables to track obstacleGrid traversal
        current_row = 0
        current_column = 0

        # Start modifying obstacleGrid in-place to the number of unique paths.
        # The number will automatically be 0 if the square is an obstacle

        # Evaluate top left corner on the diagonal
        if obstacleGrid[0][0] == 0:
            obstacleGrid[0][0] = 1
        else:
            obstacleGrid[0][0] = 0

        # Modify the first column, below the top left corner.
        # Scores are evaluated from the above square if not an obstacle
        for i in range(1, total_rows):
            if obstacleGrid[i][current_column] == 1:
                obstacleGrid[i][current_column] = 0
            else:
                obstacleGrid[i][current_column] = obstacleGrid[i - 1][current_column]

        # Modify the first row, to the right of the top left corner.
        # Scores are evaluated from the left square if not an obstacle
        for i in range(1, total_columns):
            if obstacleGrid[current_row][i] == 1:
                obstacleGrid[current_row][i] = 0
            else:
                obstacleGrid[current_row][i] = obstacleGrid[current_row][i - 1]

        current_row += 1
        current_column += 1

        # Repeat the same logic for the rest of the grid

        while current_row < total_rows and current_column < total_columns:
            # Now modify the square on the 2nd column and row, on the bottom-right
            # diagonal of the top left square. Scores are now evaluated from two squares,
            # the top and left ones
            if obstacleGrid[current_row][current_column] == 1:
                obstacleGrid[current_row][current_column] = 0
            else:
                obstacleGrid[current_row][current_column] = obstacleGrid[current_row - 1][current_column] + obstacleGrid[current_row][current_column - 1]

            for i in range(current_row + 1, total_rows):
                if obstacleGrid[i][current_column] == 1:
                    obstacleGrid[i][current_column] = 0
                else:
                    obstacleGrid[i][current_column] = obstacleGrid[i - 1][current_column] + obstacleGrid[i][current_column - 1]

            for i in range(current_column + 1, total_columns):
                if obstacleGrid[current_row][i] == 1:
                    obstacleGrid[current_row][i] = 0
                else:
                    obstacleGrid[current_row][i] = obstacleGrid[current_row][i - 1] + obstacleGrid[current_row - 1][i]

            current_row += 1
            current_column += 1

        print(obstacleGrid)
        return obstacleGrid[-1][-1]


solution = Solution()
print(solution.uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]]))
