import time
import self as self
from win10toast import ToastNotifier
from location_generate import Generate_location as gl
from tracker_gps import Gps_tracker as gt
from speed_calculation import Speed as sd
from current_gps import Gps_current as gc
from gyroscope_diff import Gyroscope as gd
import gmaps
if __name__ == '__main__':
    theft_control = input("activate theft control? Press yes if u want to activate")
    tn = ToastNotifier()
    if theft_control == "yes" or theft_control == "Yes" or theft_control == "YES":
        print("theft control is activated")
        #print("op2: speed = ",speed_value)
        change_gyroscope = gd.gyroscope(self)
        location = gl.generate_location(self)
        while True:
            change_gps = gt.gps_tracker(location)
            time.sleep(2)
            if change_gps != "not moving":
                print("bike is moving")
                tn.show_toast("alert from theft control application","Unusual activity detected: Your vehicle is moving ")
                while True:
                    time.sleep(3)
                    loc = gc.gps_current(self)
            speed_value = sd.speed(self)
            print("speed: ", speed_value)
            if speed_value != 0:
                print("vehicle is moving")
                tn.show_toast("alert from theft control application", "Unusual activity detected: Your vehicle is moving ")
                gc.gps_current(self)
            change_gyroscope = gd.gyroscope(self)
            print("change in gyro ",change_gyroscope)
            if change_gyroscope !=0:
                print("bike is moving")
                tn.show_toast("alert from theft control application", "Unusual activity detected: Your vehicle is moving ")
                gc.gps_current(self)
    else:
        exit(0)