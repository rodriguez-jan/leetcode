class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        total_changes = 0
        if not grid:
            return 0
        row_max = [0] * len(grid)
        col_max = [0] * len(grid[0])

        # Find the max in each row

        for i, row in enumerate(grid):
            row_max[i] = max(row)

            # Find the max in each column
        for j in range(len(grid[0])):
            temp_col_max = 0
            for i in range(len(grid)):
                if grid[i][j] > temp_col_max:
                    temp_col_max = grid[i][j]

            col_max[j] = temp_col_max

        # Go through entire grid and compare every cell value to respective maxes in row and cols
        # Take the min value and add the changes to a total variable

        for i, row in enumerate(grid):
            for j, col in enumerate(row):
                smallest_max = min(row_max[i], col_max[j])
                total_changes += smallest_max - grid[i][j]

        return total_changes