import unittest
from tracker_gps import Gps_tracker as gt
class Test_gps_tracker(unittest.TestCase):
    def test_gps(self):
        self.assertEqual(gt.gps_tracker({"park_latitude" : 78.66666,"park_longitude" : 45.89898,"current_latitude" : 78.66666,
                                         "current_longitude" : 45.89898}),"not moving")
        self.assertEqual(gt.gps_tracker({"park_latitude" : 78.66666,"park_longitude" : 45.89898,"current_latitude" : 78.22222,
                                         "current_longitude" : 45.89898}),"moving")
