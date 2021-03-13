class Solution(object):
    """
    simple O(n*log(n)) solution, it's not hard to see that you simply connect two sticks of the smallest length
    into one to minimize your cost. So this question is really meaningless
    """

    def connectSticks(self, sticks):
        import heapq

        heap = []
        for stick in sticks:
            heapq.heappush(heap, stick)
        cost = 0
        while len(heap) > 1:
            num1, num2 = heapq.heappop(heap), heapq.heappop(heap)
            cost += num1 + num2
            heapq.heappush(heap, num1 + num2)

        return cost