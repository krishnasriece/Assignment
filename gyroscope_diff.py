import random
class Gyroscope():
    def gyroscope(self):
        gyro_reading = [1, 2, 3, 4]
        gyro = [random.choice(gyro_reading), random.choice(gyro_reading)]
        gyro_diff = gyro[0] - gyro[1]
        return gyro_diff
