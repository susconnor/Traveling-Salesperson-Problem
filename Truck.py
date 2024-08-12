from queue import Queue
from datetime import time



class Truck:
    # Create new Truck object
    # default speed is 18 mph.
    # default max load is 16 packages.
    def __init__(self, start_time, avg_speed=18, max_packages=16):
        self.start_time = start_time
        self.end_time = time()
        self.starting_loc = 0  # this location is the hub
        self.package_list = []
        self.route = Queue()  # packages in the correct order that they should be delivered in
        self.miles_traveled = 0
        self.avg_speed = avg_speed
        self.max_packages = max_packages
