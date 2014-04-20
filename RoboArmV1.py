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

import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
import matplotlib.image as mpimg

particles_size = 3      #Size of particles displayed
scale_factor = 1.0     #Scale the image dimensions
threshhold = 0.5       #Threshold brightness value, determines which points to print. 
                                  #Higher value means lighter colors are printed.
max_recursion = 300  #Maximum length of a continuous line.
frames = 300              #The total length of time the animation runs for
interval = 1                #The interval between animation actions

arm1 = 100.0             #The length of arm 1 
arm2 = 100.0             #The length of arm 2 

theta1pos= 0.0       #The angle of servo1
theta2pos= 0.0       #The angle of servo2
theta3pos= 0.0       #The angle of servo3

rad2deg = 180/np.pi

theta1_min = 0      #offset to keep theta1 positive
pen_down  = np.pi/2     #angle when pen is down
pen_up = 0                  #angle when pen is up

image_X = []            #Used to store the x-coordinates of each particle
image_Y = []            #Used to store the y-coordinates of each particle

parse_list = []           #data structure to store list of lines that compose the image
line_list = []              #data structure to contain list of line objects in addition to list of lines that compose the image
angle_list = []           #data structure to store servo angles for robotic arm

output_file = 'output.csv'
image_location = 'images\\bernese2.png'
#read the image specified by the global variables
read_image = mpimg.imread(image_location)

fig = plt.figure()

# initialization function: plot the background of each frame
def init():
    # print "Started init"
    global ax
    
    # First set up the figure, the axis, and the plot element we want to animate
    ax = plt.axes(xlim=(-1, len(read_image[0])/scale_factor) , ylim=(0,  1+ len(read_image)/scale_factor))

    # line, = ax.plot([], [], lw=2)

    for x_list, y_list in parse_list:
        anim_line, = ax.plot([], [], lw=2)

        line_list.append((x_list, y_list, anim_line))
    
    # line.set_data([], [])
    
    return_line = []
    for x_list, y_list, anim_line in line_list:
        anim_line.set_data(x_list, y_list)
        return_line.append(anim_line)
    
    # print "Finished init"
    return tuple(return_line)
    # return line, 

# animation function.  This is called sequentially
def animate(i):
    return_line = []
    
    # global image_X, image_Y
    # line.set_data(image_X[0:i], image_Y[0:i])
    
    for x_list, y_list, anim_line in line_list:
        anim_line.set_data(x_list[0:i], y_list[0:i])
        return_line.append(anim_line)
        
    return tuple(return_line)
    # return line,
    
# parses a pre-defined image into a list of lines as defined by x, y groupings
# (the x-coordinates are stored on a list and the y coordinates are stored on a separate list)
def parse_image():
    global scale_factor, threshhold, read_image
    
    y_index = 0
    x_index = 0
    recursion_level = 0
    
    # print read_image
    
    # iterate through image array
    while y_index < len(read_image):
        # print row
        x_index = 0
        while x_index < len(read_image[y_index]):
            
            if sum(read_image[y_index][x_index])/4 <= threshhold:
                line_X = []
                line_Y = []
                
                parse_recursive(y_index, x_index, recursion_level, line_X, line_Y)
                parse_list.append((line_X,line_Y))
                
                # print "Finished Line\n"
            x_index += 1
        y_index += 1

# recursively determine if the points surrounding the current point should be added to current line
# uses a pre-defined thresh hold limit
def parse_recursive(input_y, input_x, recursion_level, line_X, line_Y):
    global scale_factor, threshhold, read_image
    
    # print input_y, input_x
    
    # store current input
    image_X.append((input_x)/scale_factor)
    image_Y.append((len(read_image) - input_y)/scale_factor)
    
    line_X.append((input_x)/scale_factor)
    line_Y.append((len(read_image) - input_y)/scale_factor)
    
    #erase from image array
    read_image[input_y][input_x] = [1, 1, 1, 1]
    
    x_min = 0
    x_max = len(read_image[0])
    y_min = 0
    y_max = len(read_image)
    
    if(recursion_level < max_recursion):
        recursion_level += 1
        
        # print recursion_level
    
        # top left
        if input_y > y_min and input_x > x_min and sum(read_image[input_y - 1][input_x - 1])/4 <= threshhold:
            # print "top-left"
            parse_recursive(input_y - 1, input_x - 1, recursion_level, line_X, line_Y)
        #top
        elif input_y > y_min and sum(read_image[input_y - 1][input_x])/4 <= threshhold:
            # print "top"
            parse_recursive(input_y - 1, input_x, recursion_level, line_X, line_Y)
        #top right
        elif input_y > y_min and input_x < x_max-1 and sum(read_image[input_y - 1][input_x + 1])/4 <= threshhold:
            # print "top-right"
            parse_recursive(input_y - 1, input_x + 1, recursion_level, line_X, line_Y)
        # right
        elif input_x < x_max-1 and sum(read_image[input_y][input_x + 1])/4 <= threshhold:
            # print "right"
            parse_recursive(input_y, input_x + 1, recursion_level, line_X, line_Y)
        # bot right
        elif input_x < x_max-1 and input_y < y_max-1 and sum(read_image[input_y + 1][input_x + 1])/4 <= threshhold:
            # print "bot-right"
            parse_recursive(input_y + 1, input_x + 1, recursion_level, line_X, line_Y)
        # bot
        elif input_y < y_max-1 and sum(read_image[input_y + 1][input_x])/4 <= threshhold:
            # print "bot"
            parse_recursive(input_y + 1, input_x, recursion_level, line_X, line_Y)
        # bot left
        elif input_y < y_max-1 and input_x > x_min and sum(read_image[input_y + 1][input_x - 1])/4 <= threshhold:
            # print "bot-left"
            parse_recursive(input_y + 1, input_x - 1, recursion_level, line_X, line_Y)
        # left
        elif input_x > x_min and sum(read_image[input_y][input_x - 1])/4 <= threshhold:
            # print "left"
            parse_recursive(input_y, input_x - 1, recursion_level, line_X, line_Y)
        # else:
            # print "none"

# takes as input the parse_list containing lines that compose the parsed image
# generates a list of angles for the three servos of the robot arm
def generate_arm_angles():
    global pen_up, pen_down

    
    # angle_list
    for x_list, y_list in parse_list:
        x_init = x_list[0]
        y_init = y_list[0]
        theta1_final = 0
        theta2_final = 0
            
        #initially, pen is over first point but does not touch it (such a tease)
        theta3pos = pen_up
        theta2pos =2.0 * np.arctan(np.sqrt( ((arm1 + arm2)**2 - (x_init**2 + y_init**2)) / ((x_init**2 + y_init**2) - (arm1 - arm2)**2) ))
        theta1pos = np.arctan2(y_init,x_init) - np.arctan2(arm2*np.sin(theta2pos), arm1 + arm2 * np.cos(theta2pos))

        append_angle(theta1pos,theta2pos,theta3pos)
                
        for point_y in y_list:
            for point_x in x_list:
                theta3pos = pen_down
                theta2pos = 2.0 * np.arctan(np.sqrt( ((arm1 + arm2)**2 - (point_x**2 + point_y**2)) / ((point_x**2 + point_y**2) - (arm1 - arm2)**2) ))
                theta1pos = np.arctan2(point_y,point_x) - np.arctan2(arm2*np.sin(theta2pos), arm1 + arm2 * np.cos(theta2pos))            
                
                theta2_final = theta2pos
                theta1_final = theta1pos
                
                append_angle(theta1pos,theta2pos,theta3pos)
                
        append_angle(theta1_final,theta2_final,pen_up)

def append_angle(theta1 = -1, theta2 = -1, theta3 = -1):
    global theta1_min
    
    # if((theta1 < 0) or (theta2 < 0) or (theta3 < 0)):
        # print "Tried to append negative angle"
        # return
    
    theta1 = (np.floor(rad2deg * theta1 * 100) / 100)
    theta2 = (np.floor(rad2deg * theta2 * 100) / 100)
    theta3 = (np.floor(rad2deg * theta3 * 100) / 100)    
    
    angle_list.append([theta1,theta2,theta3])
    
    if theta3 < theta1_min:
        theta1_min = theta3
    
        
parse_image()

# # call the animator.  blit=True means only re-draw the parts that have changed.
# anim = animation.FuncAnimation(fig, animate, init_func=init,
                               # frames=frames, interval=interval, blit=False)

# plt.show()

generate_arm_angles()

output_fh= open(output_file, 'w')

for theta1, theta2, theta3 in angle_list:
    # print angle_set
    #correct theta1 to ensure it stays positive
    theta1 = theta1 - theta1_min
    
    output_line = theta1,theta2,theta3
    output_fh.write(str(output_line))
    output_fh.write("\n")
    
output_fh.close()



    
    
    
    