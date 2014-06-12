#!/usr/bin/env python3

"""
This is a program written by William Millard for silly purposes

It switches wallpapers based on a timer
"""

import os
import sys
import time
import random

"""
Constants
"""
kSleepLowerBound = 60 #one minute in seconds
kSleepUpperBound = 54300 #six hours in seconds

"""
Globals
"""
timer = 60 * 5 #five minutes in seconds
directory = 'Wallpapers'
wallpapers = []

def changeWallpaper():
    if not os.fork():
        print("not parent!")

def main(args):
    for arg in sys.argv:
        print('unsupported arg %s', arg)

    for dirpath, dirname, filename in os.walk(directory):
        for individual_file in filename:
            wallpapers.append(dirpath + '/' + individual_file)

    while (True):
        changeWallpaper()

        if timer == 0: #if timer is not set, sleep for a random period
            time.sleep(random.randint(kSleepLowerBound,kSleepUpperBound))
        else:
            time.sleep(timer)

main(sys.argv[1::])
