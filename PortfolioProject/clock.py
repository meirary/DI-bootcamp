class JewishClock:
    def __init__(self, day=0, moon=0, sun=0, hour=0):
        self.day = day
        self.moon = moon
        self.sun = sun
        self.hour = hour

    def tick(self):
        self.hour += 1
        if self.hour >= 1800:
            self.hour = 0
            self.sun += 1
            if self.sun >= 21600:
                self.sun = 0
                self.moon += 1
                if self.moon >= 21600:
                    self.moon = 0
                    self.day += 1
                    if self.day >= 43200:
                        self.day = 0

    def get_time(self):
        return f"Day: {self.day}, Moon: {self.moon}, Sun: {self.sun}, Hour: {self.hour}"

# Create a JewishClock instance
clock = JewishClock()

# Run the clock for a while
for i in range(43200):
    clock.tick()

# Get and print the time
print(clock.get_time())
