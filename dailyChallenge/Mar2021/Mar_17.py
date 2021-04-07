"""
Generate Random Point in a Circle

Description: Given the radius and x-y positions of the center of a circle,
write a function randPoint which generates a uniform random point in the circle.

Input:
["Solution","randPoint","randPoint","randPoint"]
[[1,0,0],[],[],[]]
Output: [null,[-0.72939,-0.65505],[-0.78502,-0.28626],[-0.83119,-0.19803]]

Solution: nothing to say about the solution, just straightforward
"""
from random import uniform
class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.radius = radius
        self.x_center = x_center
        self.y_center = y_center

    def randPoint(self) -> List[float]:
        x_rand, y_rand = uniform(self.x_center - self.radius, self.radius + self.x_center), \
                         uniform(self.y_center - self.radius, self.radius + self.y_center)
        while self.euclideanDistance([self.x_center, self.y_center], [x_rand, y_rand]) > self.radius:
            x_rand, y_rand = uniform(self.x_center - self.radius, self.radius + self.x_center), \
                             uniform(self.y_center - self.radius, self.radius + self.y_center)
        return [x_rand, y_rand]

    def euclideanDistance(self, p1: List[float], p2: List[float]) -> float:
        if len(p1) == len(p2) == 2:
            return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)
        return -1

# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()