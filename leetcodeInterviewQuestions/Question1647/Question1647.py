class Solution:
    def minDeletions(self, s: str) -> int:
        freqs = list(map(lambda x: -x, Counter(s).values()))
        heapify(freqs)

        result = 0
        bestSlot = -min(freqs)  # max from freqs heap
        while freqs and bestSlot > 0:
            freq = -heappop(freqs)
            result += max(0,
                          freq - bestSlot)  # if the slot is larger than the frequency, simply use the slot at the frequency instead (since we can only subtract from the frequency)
            bestSlot = min(freq - 1, bestSlot - 1)  # the next available best slot is 1 below the slot just used

        return result - sum(freqs)