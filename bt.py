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
verbosity = 0
wallpapers = []

def changeWallpaper():
    if not os.fork():
        random.seed()
        os.execlp('hsetroot', 'hsetroot', '-fill', random.choice(wallpapers))

def main(args):
    for arg in args:
        if arg == '-h' or arg == '--help':
            print('Unsupported at this time')
        elif arg == '-v' or arg == '--verbose':
            verbosity += 1
        elif arg == '-f' or arg == '--folder':
            print('Unsupported at this time')
        elif arg == '-i' or arg == '--interval':
            print('Unsupported at this time')
        else:
            print(sys.argv[0], '- unsupported arg:', arg)
            sys.exit(1)

    for dirpath, dirname, filename in os.walk(directory):
        for individual_file in filename:
            wallpapers.append(dirpath + '/' + individual_file)

    while (True):
        changeWallpaper()

        if timer == 0: #if timer is not set, sleep for a random period
            time.sleep(random.randint(kSleepLowerBound,kSleepUpperBound))
        else:
            time.sleepeep(timer)

main(sys.argv[1:])
