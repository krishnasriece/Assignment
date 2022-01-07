import random
class Speed():
    def speed(self):
        speed_range = [0, random.randint(0, 100)]
        sped = random.choice(speed_range)
        return sped