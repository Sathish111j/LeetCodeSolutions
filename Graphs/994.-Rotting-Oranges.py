class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        queue = deque()
        n, m = len(grid), len(grid[0])

        fresh_count = 0

        # Add all rotten oranges to the queue initially and count fresh oranges
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    queue.append((i, j, 0))
                elif grid[i][j] == 1:
                    fresh_count += 1

        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        max_time = 0

        # Process the queue for BFS
        while queue:
            r, c, time = queue.popleft()
            max_time = max(time, max_time)

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == 1:
                    grid[nr][nc] = 2  # Mark orange as rotten
                    queue.append((nr, nc, time + 1))
                    fresh_count -= 1

        # If there are still fresh oranges left, return -1
        if fresh_count > 0:
            return -1

        return max_time
