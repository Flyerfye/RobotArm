# Drawing an Image
# Issa Beekun, March 2014 
 
 
# Consider making the path thingy a depth first search
 
# **image parsing algorithm**
# Load picture/image
# Starting a pointer in upper left corner, check if current pixel is filled
# If so:
#   - Draw current pixel
#   - Erase it from map of pixels to be drawn
#   - Search adjacent 8 pixels starting at top left pixel and circling clockwise
#   - If an adjacent pixel is found:
#       > repeat process
#     Else:
#       > continue search by column then row
#  Else:
#   - Continue search by column then row, repeat process
#  Keep track where the pointer is, when it reaches the end the program finishes
#  
#  arms are 1.25" each

# **arm drawing algorithm**
# Take the list of lines that have been generated from the parsed image
# For each line:
#   - Move to the angles for servo1 and servo2 that define first point
#   - Move servo3 (attached to the drawing implement) so it just touches the paper
#   - Iterate through all points/servo angles for that line
#   - After last line is finished, stay at current point but move servo3 to lift drawing implement off paper

from Modules import arm_manipulation as a_m
from Modules import arm_simulation as a_s
from Modules import image_manipulation as i_m
import serial
import numpy as np
import time

# image_location = 'images\\sb_small.png'
# image_location = 'images\\bernese2.png'
# image_location = 'images\\test_imageIssa.png'
image_location = 'images\\test_image13.png'

read_image = []           
parse_list = []           #data structure to store list of lines that compose the image


read_image, parse_list = i_m.parse_image(image_location)
# read_image, parse_list = a_s.test_image()

a_s.display_image(input_image = read_image, input_parse_list = parse_list)
# #  
angle_list = a_m.generate_arm_angles(parse_list)
# angle_list = []
# #      
# a_s.simulate_arm(input_angle_list = angle_list)

if(1 != 1):
    serial_connection = serial.Serial("COM4", 9600)
    input_character  = " "
    connected = False
         
    # loop until the arduino is ready for input
    while not connected:
        while input_character != 'X':
            input_character = serial_connection.read()
                 
        connected = True
         
    count = 0
    theta1 = 90
             
    for theta1, theta2, theta3, xi, yi in angle_list:
#     while(count <= 10) and theta1<160:

#         theta1 = 00
#         theta2 = 45
#         theta3 = 90
#         theta1 = int(raw_input('Theta1?'))
# #         theta2 = int(raw_input('Theta2?'))
#         theta3 = int(raw_input('Theta3?'))
             
        x1 = a_m.arm1*np.cos(np.radians(theta1))
        y1 = a_m.arm1*np.sin(np.radians(theta1))
        xp = a_m.arm2*np.cos(np.radians(theta1 + theta2))
        yp = a_m.arm2*np.sin(np.radians(theta1 + theta2))
             
        x2 = x1 + xp
        y2 = y1 + yp
             
        print "[", theta1,",", theta2,",", theta3,"] => (", '%.1f' % round(x2, 2),", ", '%.1f' % round(y2, 2),"), "
#             print "(", '%.1f' % round(x2, 2),", ", '%.1f' % round(y2, 2),"), "
              
        a_m.write_angle('A', theta1, serial_connection)
        a_m.write_angle('B', theta2, serial_connection)
        a_m.write_angle('C', theta3, serial_connection)
        
#         raw_input('Next?')
        
        count += 1
        time.sleep(0.1)
         
    # close the port and end the program
    serial_connection.close()

print "All done."   
    
    