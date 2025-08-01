class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        q = deque([])
        for i, num in enumerate(tickets):
            q.append((num, i))

        t = 0
        while q:
            ticket, i = q.popleft()
            ticket -= 1
            t += 1
            if ticket > 0:
                q.append((ticket, i))
            if i == k and ticket == 0:
                return t
        return t

        