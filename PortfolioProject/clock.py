import astral
import datetime


class JewishClock:
    def __init__(self, day=0, moon=0, sun=0, hour=0):
        self.day = day
        self.moon = moon
        self.sun = sun
        self.hour = hour

    def tick(self):
        self.hour += 1
        if self.hour >= 1080:
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


# Exercises 4


def display_current_date():
    current_date = datetime.date.today()
    print("Current Date:", current_date)

display_current_date()

# Exercises 5

def time_left_until_Pesaj_5784():
    current_datetime = datetime.datetime.now()

    next_year = current_datetime.year + 1
    target_date = datetime.datetime(next_year, 4, 24)

    time_difference = target_date - current_datetime

    days = time_difference.days
    hours, remainder = divmod(time_difference.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    print(f"Pesaj 5784 is in {days} days and {hours}:{minutes:02}:{seconds:02} hours.")

time_left_until_Pesaj_5784()

# Exercises 6

def minutes_lived(birthdate):
    birthdate = datetime.datetime.strptime(birthdate, "%d-%m-%Y")

    current_datetime = datetime.datetime.now()

    time_difference = current_datetime - birthdate

    total_minutes_lived = time_difference.total_seconds() / 60

    return total_minutes_lived


birthdate = "19-09-1981"  # Replace with the user's birthdate in the specified format
minutes = minutes_lived(birthdate)
print(f"You have lived for approximately {minutes:.2f} minutes.")