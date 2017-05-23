#!/usr/bin/python

import smbus
import math
import time
import subprocess


# Power management registers
power_mgmt_1 = 0x6b
power_mgmt_2 = 0x6c
sensitive4g = 0x1c

class MPU6050Read():
    
    def __init__(self,address,bus=1):
        self._address=address
        self._bus=smbus.SMBus(bus)
        self._bus.write_byte_data(self._address, power_mgmt_1, 0)
        '''
        try:
            self._bus.write_byte_data(self._address, power_mgmt_1, 0)
        except IOError:
            subprocess.call(['i2cdetect','-y','1'])
        '''        

    def _read_byte(self,adr):
        return self._bus.read_byte_data(self._address, adr)


    def _read_word(self,adr):
        high = self._bus.read_byte_data(self._address, adr)
        low = self._bus.read_byte_data(self._address, adr+1)
        val = (high << 8) + low
        return val

    def read_word_2c(self,adr):
        val = self._read_word(adr)
        if (val >= 0x8000):               #MPU6050 16bits register data range +32768~-32768 value larger than 32768 transfer it to negative
            return -((65535 - val) + 1)
        else:
            return val
    def dist(a,b):
        return math.sqrt((a*a)+(b*b))

    def get_y_rotation(x,y,z):
        radians = math.atan2(x, dist(y,z))
        return -math.degrees(radians)

    def get_x_rotation(x,y,z):
        radians = math.atan2(y, dist(x,z))
        return math.degrees(radians)

    def print_value(gyro_xout,gyro_yout,gyro_zout,accel_xout,accel_yout,accel_zout):
        print "gyro_xout : ", gyro_xout, " scaled: ", (gyro_xout / 131)
        print "gyro_yout : ", gyro_yout, " scaled: ", (gyro_yout / 131)
        print "gyro_zout : ", gyro_zout, " scaled: ", (gyro_zout / 131)
        print "accel_xout: ", accel_xout, " scaled: ", accel_xout_scaled
        print "accel_yout: ", accel_yout, " scaled: ", accel_yout_scaled
        print "accel_zout: ", accel_zout, " scaled: ", accel_zout_scaled

################################     main      ######################################
'''
    bus = smbus.SMBus(1) # or bus = smbus.SMBus(1) for Revision 2 boards
    address = 0x68       # This is the address value read via the i2cdetect command

# Now wake the 6050 up as it starts in sleep mode
    bus.write_byte_data(address, power_mgmt_1, 0)

    while True:
        bus.write_byte_data(address, power_mgmt_1, 0) #reset to +-2g mode
        time.sleep(0.1)
        gyro_xout = read_word_2c(0x43)
        gyro_yout = read_word_2c(0x45)
        gyro_zout = read_word_2c(0x47)

        print "gyro_xout : ", gyro_xout, " scaled: ", (gyro_xout / 131)
        print "gyro_yout : ", gyro_yout, " scaled: ", (gyro_yout / 131)
        print "gyro_zout : ", gyro_zout, " scaled: ", (gyro_zout / 131)

        accel_xout = read_word_2c(0x3b)
        accel_yout = read_word_2c(0x3d)
        accel_zout = read_word_2c(0x3f)
        accel_xout_scaled = accel_xout / 16384.0
        accel_yout_scaled = accel_yout / 16384.0
        accel_zout_scaled = accel_zout / 16384.0
        
        if(accel_xout>=32768||accel_yout>=32768||accel_zout>=32768){
            write_byte_data(address,sensitive4g,0b00010000)  #change to +-4g mode
            accel_xout = read_word_2c(0x3b)
            accel_yout = read_word_2c(0x3d)
            accel_zout = read_word_2c(0x3f)
            accel_xout_scaled = accel_xout / 8192.0
            accel_yout_scaled = accel_yout / 8192.0
            accel_zout_scaled = accel_zout / 8192.0
            
        }

        print "accel_xout: ", accel_xout, " scaled: ", accel_xout_scaled
        print "accel_yout: ", accel_yout, " scaled: ", accel_yout_scaled
        print "accel_zout: ", accel_zout, " scaled: ", accel_zout_scaled

        print "x rotation: " , get_x_rotation(accel_xout_scaled, accel_yout_scaled, accel_zout_scaled)
        print "y rotation: " , get_y_rotation(accel_xout_scaled, accel_yout_scaled, accel_zout_scaled)
'''
