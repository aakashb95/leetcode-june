class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        r = len(dungeon)
        c = len(dungeon[0])

        solver = [[0 for i in range(c)] for i in range(r)]

        solver[r - 1][c - 1] = (
            1 if dungeon[r - 1][c - 1] > 0 else 1 - dungeon[r - 1][c - 1]
        )

        for i in range(r - 2, -1, -1):
            solver[i][c - 1] = max(solver[i + 1][c - 1] - dungeon[i][c - 1], 1)

        for j in range(c - 2, -1, -1):
            solver[r - 1][j] = max(solver[r - 1][j + 1] - dungeon[r - 1][j], 1)

        for i in range(r - 2, -1, -1):
            for j in range(c - 2, -1, -1):
                solver[i][j] = max(
                    min(solver[i + 1][j], solver[i][j + 1]) - dungeon[i][j], 1
                )

        return solver[0][0]


# Dungeon = [[-2,-3,3],[-5,-10,1],[10,30,-5]]

