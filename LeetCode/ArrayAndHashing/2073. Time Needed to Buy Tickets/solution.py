class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        queue = collections.deque()
        for i in range(len(tickets)):
            queue.append(i)

        time = 0
        while queue:
            front = queue.popleft()
            tickets[front] -= 1
            time += 1
            
            if front == k and tickets[front] == 0:
                return time
            
            if tickets[front] == 0:
                continue

            queue.append(front)
