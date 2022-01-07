class Gps_tracker():
    def gps_tracker(location):
        print("current at latitude ",location["current_latitude"],"longitude",location["current_longitude"])
        diff_1 = location["park_latitude"] - location["current_latitude"]
        diff_2 = location["park_longitude"]-location["current_longitude"]
        if (diff_1 != 0.00000) or (diff_2 != 0.00000):
            change_in_gps = "moving"
        else:
            change_in_gps = "not moving"
        return change_in_gps
