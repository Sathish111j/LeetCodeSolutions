class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])
        distances = [[float('inf')] * cols for _ in range(rows)]
        queue = deque()
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    distances[r][c] = 0
                    queue.append((r, c, 0))  # (row, col, distance)


        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while queue:
            r, c, dist = queue.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    if distances[nr][nc] > dist + 1:
                        distances[nr][nc] = dist + 1
                        queue.append((nr, nc, dist + 1))  

        return distances