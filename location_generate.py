import random
class Generate_location():
    def generate_location(self):
        park_latitude = round(random.uniform(-90, 90), 5)
        park_longitude = round(random.uniform(-90, 90), 5)
        print("parked at latitude ", park_latitude, "longitude", park_longitude)
        current_latitude = round(random.uniform(-90, 90), 5)
        current_longitude = round(random.uniform(-90, 90), 5)
        location = {"park_latitude": park_latitude, "park_longitude": park_longitude,
                    "current_latitude": current_latitude, "current_longitude": current_longitude}
        return location
