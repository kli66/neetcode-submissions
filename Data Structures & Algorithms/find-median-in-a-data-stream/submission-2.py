import heapq


class MedianFinder:

    def __init__(self):
        self.low_buffer = []
        self.high_buffer = []
        
    def _balance(self):
        if not self.low_buffer or not self.high_buffer:
            return

        while self.low_buffer[0] * -1 > self.high_buffer[0]:
            to_low = heapq.heappushpop(self.high_buffer, heapq.heappop(self.low_buffer) * -1)
            heapq.heappush(self.low_buffer, to_low*-1)
            
            return

    def addNum(self, num: int) -> None:
        if len(self.low_buffer) == len(self.high_buffer):
            heapq.heappush(self.low_buffer, num * -1)
        else:
            if len(self.low_buffer) > len(self.high_buffer):
                heapq.heappush(self.high_buffer, num)
            else:
                heapq.heappush(self.low_buffer, num * -1)
        self._balance()


    def findMedian(self) -> float:
        if not self.low_buffer and not self.high_buffer:
            raise Exception
        
        
        if len(self.low_buffer) == len(self.high_buffer):
            return (self.low_buffer[0]*-1 + self.high_buffer[0])/2
        else:
            # not handling the single element case?
            return self.low_buffer[0] * -1

