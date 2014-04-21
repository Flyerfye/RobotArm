'''
Created on 2011-12-02

@author: Bobby Wood
'''

# import the serial library
import serial

# Boolean variable that will represent 
# whether or not the arduino is connected
connected = False

count = 0

# open the serial port that your ardiono 
# is connected to.
ser = serial.Serial("COM4", 9600)

var = " "

# loop until the arduino tells us it is ready
while not connected:
    while var != 'X':
        var = ser.read()
    connected = True

while(count < 3):
    raw_input("Press enter to continue...")
    # Tell the arduino to blink!
    ser.write("[3.12]")

    var = ser.read()
    print var
    # Wait until the arduino tells us it 
    # is finished blinking
    while var != 'X':
        var = ser.read()
        
        # ser.read()
        print var
        
    print var
    count += 1

# close the port and end the program
ser.close()