class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        hourDegree = (hour%12)*30 + (minutes)/2
        minuteDegree = minutes*6
        diff = abs(hourDegree-minuteDegree)
        return diff if diff < 180 else 360-diff