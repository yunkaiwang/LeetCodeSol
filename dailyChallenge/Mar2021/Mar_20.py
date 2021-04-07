"""
Design Underground System

Not much to say, straight forward solution after
understanding the requirement, O(1) time with
potential O(n) space. But there is no other
optimization we can do other than deleting each
entry after the tour has completed.
"""
class UndergroundSystem:

    def __init__(self):
        self.checkedIn = {}
        self.completeTour = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        if id in self.checkedIn:
            return  # the user with id has not completed a tour yet, should not check in again

        self.checkedIn[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        if id not in self.checkedIn:
            return  # the user is not in an active tour

        (origin, start_t) = self.checkedIn[id]
        del self.checkedIn[id]  # the tour has completed

        key = origin + "+" + stationName
        if key in self.completeTour:
            self.completeTour[key][0] += 1.0
            self.completeTour[key][1] += t - start_t
        else:
            self.completeTour[key] = [1.0, t - start_t]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        key = startStation + "+" + endStation
        if key not in self.completeTour:
            return -1  # not such tour exist
        return self.completeTour[key][1] / self.completeTour[key][0]

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)