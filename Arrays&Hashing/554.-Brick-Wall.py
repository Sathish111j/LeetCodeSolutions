class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        alligned=defaultdict(int) # to find max alligned brick vertically

        for row in wall:
            edge_position=0
            for brick_length in row[:-1]: # skipping last row to avoid alligning with wall at last 
                edge_position+=brick_length
                alligned[edge_position]+=1

        max_alligned=max(alligned.values(),default=0) # finding the max alligned

        return len(wall)-max_alligned  # returning the no of rows - max alligned gives the minimum row to cross


        