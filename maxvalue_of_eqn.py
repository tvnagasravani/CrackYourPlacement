import heapq

class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        # Priority queue to store pairs (-yi + xi, xi)
        pq = []  
        max_value = float('-inf')

        for x, y in points:
            # Remove elements from the queue if xj - xi > k
            while pq and x - pq[0][1] > k:
                heapq.heappop(pq)
            
            # Update the maximum value if the queue is not empty
            if pq:
                max_value = max(max_value, y + x - pq[0][0])

            # Push the current element (-yi + xi, xi) to the queue
            heapq.heappush(pq, (-(y - x), x))

        return max_value
