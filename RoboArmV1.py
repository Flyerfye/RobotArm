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

image_location = 'images\\maze.png'

parse_list = []           #data structure to store list of lines that compose the image


read_image, parse_list = i_m.parse_image(image_location)
    
a_s.display_image(input_image = read_image, input_parse_list = parse_list)

# read_image, parse_list = i_m.parse_image(image_location)
# a_s.display_image(read_image, parse_list)

a_m.generate_arm_angles(parse_list)


# serial_connection = serial.Serial("COM4", 9600)
# input_character  = " "
# connected = False

# # loop until the arduino is ready for input
# while not connected:
    # while input_character != 'X':
        # input_character = serial_connection.read()
        
    # connected = True

# count = 0
    
# theta1pos= 0.0       #The angle of servo1
# theta2pos= 0.0       #The angle of servo2
# theta3pos= 0.0       #The angle of servo3
    
# for theta1, theta2, theta3, xi, yi in angle_list:
    # if(count >= 0):
        # # corrects theta1 so angle is in a quadrant that the arm can reach
        # theta1 += 90
        
        # # corrects theta2 for offset of pen from center of arm
        # theta2 += 34.56
        
        # if theta3 == 0:
            # print "\nNew Line"
        
        # print count, ":\t[", theta1,",", theta2,",", theta3,"]"
        
        # x1 = arm1*np.cos(theta1/rad2deg)
        # y1 = arm1*np.sin(theta1/rad2deg)
        # xp = arm2*np.cos(theta1 + theta2)
        # yp = arm2*np.sin(theta1 + theta2)
        
        # x2 = x1 + xp
        # y2 = y1 + yp
        
        # print "Theta1\t", theta1," (", x1,", ", y1,")"
        # print "Theta2\t", theta2," (", x2,", ", y2,")\n"
        
        # write_angle('A', theta1)
        # write_angle('B', theta2)
        # write_angle('C', theta3)
        
        # # raw_input("[%.2f, %.2f, %.2f]" % (theta1, theta2, theta3))
        
        
        # count += 1

# # close the port and end the program
# serial_connection.close()


    
    
    
    