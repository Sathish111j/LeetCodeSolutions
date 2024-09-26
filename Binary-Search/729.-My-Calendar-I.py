class MyCalendar:

    def __init__(self):
        # self.bookings=[]
        self.bookings=[(-1,-1),(float("inf"),float("inf"))]

    def book(self, start: int, end: int) -> bool:
        # for s , e in self.bookings:
        #     if max(s,start)<min(e ,end):
        #         return False
        # self.bookings.append((start,end))
        # return True

        index = bisect_left(self.bookings, (start, end))

        # Check for clash with previous booking (if any)
        if start < self.bookings[index - 1][1]:
            return False

        # Check for clash with next booking (if any)
        if end > self.bookings[index][0]:
            return False

        # No clash found, insert the new booking at the appropriate position
        self.bookings.insert(index, (start, end))
        return True

        
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)