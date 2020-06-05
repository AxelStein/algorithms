class Event:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __str__(self):
        return "{} - {}".format(self.start, self.end)

    def __repr__(self):
        return str(self)


calendar1 = [Event("09:00", "10:30"), Event("12:00", "13:00"), Event("16:00", "18:00")]
con1 = ("09:00", "20:00")
calendar2 = [Event("10:00", "11:30"), Event("12:30", "14:30"), Event("14:30", "15:00"), Event("16:00", "17:00")]
con2 = ("10:00", "18:30")

# merge lists
calendar = calendar1 + calendar2

# add constraints
con_start = max(con1[0], con2[0])
calendar.append(Event(con_start, con_start))

con_end = min(con1[1], con2[1])
calendar.append(Event(con_end, con_end))

# sort list
calendar.sort(key=lambda e: (e.start, e.end))
# print(calendar)

# merge events
i = 0
while i < len(calendar) - 1:
    e = calendar[i]
    n = calendar[i + 1]
    if n.start <= e.end:
        calendar.pop(i + 1)
        e.end = n.end
    else:
        i += 1

# print(calendar)

# find spaces
output = []
i = 0
while i < len(calendar) - 1:
    s = calendar[i].end
    e = calendar[i + 1].start
    output.append(Event(s, e))
    i += 1

print(output)
