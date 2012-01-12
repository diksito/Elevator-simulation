#!/usr/bin/python

import threading
import os
import sys
from sys import stdin
from time import sleep

class Building():
    def __init__(self, maxfloor=12 ):
        self.maxfloor = maxfloor
        self.elevators = [ Elevator(0.3, 6),
                           Elevator(0.4, 4),
                           Elevator(0.4, 4) ]

        print "starting elevators..."
        
        for e in self.elevators:
            e.start()

        mtread = threading.Thread(None, Building.monitor, None, [self] )
        mtread.start()       
        
    def elevatorcall( self, destfloor ):
        print " calling elevator to floor {0} ".format(destfloor)
        
        # assert (destfloor < self.maxfloor)
        for e in self.elevators:
            if (not(e.moving)):
                e.gotofloor(float(destfloor))
                break

    def monitor(self) :
        while (True) :
            #os.system('clear')
            #print "elevator simulator v 0.1"
            #print "input: c [floor] or g [floor] to call to floor "
            #print "input: q to exit "

            #print " ----------- "
            for e in self.elevators :
                print (e)

            print ">";    
            sleep(2)

class Elevator ( threading.Thread ) :
    def __init__(self, speed = 0.2, capacity = 4, floor = 0):
        self.floor = floor
        self.speed = speed
        self.capacity = capacity
        self.moving = False
        self.destfloor = floor
        threading.Thread.__init__(self)
        print "creating Elevator with : "
        print "\tspeed {0} floors/sec ".format(str(speed)) 
        print "\tcapacity {0} ".format(capacity)

    #def __str__ (self):
    #    return " Elevator ({0}, {1}, {2} ) ".format(self.moving, self.floor, self.destfloor)

    def __str__ (self):
        return " Elevator ({0}, {1}) ".format(self.floor, self.destfloor)

    def run( self ) :
        while (True):
            if (self.moving) :
                sleep( 0.1 ) 
                if (self.destfloor > self.floor) :
                    self.floor = self.floor + ( self.speed / 10.0 )
                else :
                    self.floor = self.floor - ( self.speed / 10.0 )
                    
                if (float(abs(float(self.destfloor)-float(self.floor))) <= float(self.speed)):
                    self.floor = self.destfloor
                    self.moving = False

    def gotofloor( self, floor ):
        self.destfloor = float(floor)
        self.moving = True

b = Building()
while (True):
    c = sys.stdin.read(1)
    if (c == 'c' or c == 'g'):
        print "going to floor..."
        floor = sys.stdin.readline()
        b.elevatorcall(floor)
        print floor
    if (c == 'q'):
        print "goodbye"
        for t in b.elevators :
            t.daemon()
        exit()
        break
