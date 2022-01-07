import random
class Gps_current():
    def gps_current(self):
        current_latitude = round(random.uniform(-90, 90), 1)
        current_longitude = round(random.uniform(-90, 90), 1)
        print("current at latitude ", current_latitude, "longitude", current_longitude)
        current_location = [current_latitude,current_longitude]
        return current_location