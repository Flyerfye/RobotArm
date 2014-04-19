# Drawing an Image
# Issa Beekun, March 2014 
 
 
# Consider making the path thingy a depth first search
 
# Drawing algorithm

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

import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
import matplotlib.image as mpimg

particles_size = 3      #Size of particles displayed
scale_factor = 1.0     #Scale the image dimensions
threshhold = 0.5       #Threshold brightness value, determines which points to print. 
                                    #Higher value means lighter colors are printed.
max_recursion = 300  #Maximum length of a continuous line.
frames = 300            #The total length of time the animation runs for
interval = 1           #The interval between animation actions

image_X = []            #Used to store the x-coordinates of each particle
image_Y = []            #Used to store the y-coordinates of each particle

parse_list = []              #data structure to store list of lines that compose the image
line_list = []              #data structure to contain list of line objects in addition to list of lines that compose the image

image_location = 'images\\bernese.png'
#read the image specified by the global variables
read_image = mpimg.imread(image_location)

# First set up the figure, the axis, and the plot element we want to animate
fig = plt.figure()
ax = plt.axes(xlim=(-1, len(read_image[0])/scale_factor) , ylim=(0,  1+ len(read_image)/scale_factor))
# ax = plt.axes(xlim=(-1, 100) , ylim=(0,  100))

# line, = ax.plot([], [], lw=2)

# parse_list, = ax.plot([], [], lw=2)

# initialization function: plot the background of each frame
def init():
    print "Started init"
    # line.set_data([], [])
    
    return_line = []
    for x_list, y_list, anim_line in line_list:
        anim_line.set_data(x_list, y_list)
        # anim_line.set_data([], [])
        return_line.append(anim_line)
    
    print "Finished init"
    return tuple(return_line)
    # return line, 
    # return particles,

# animation function.  This is called sequentially
def animate(i):
    print i
    return_line = []
    
    # global image_X, image_Y
    # line.set_data(image_X[0:i], image_Y[0:i])
    
    for x_list, y_list, anim_line in line_list:
        anim_line.set_data(x_list[0:i], y_list[0:i])
        return_line.append(anim_line)
        
    # return line, return_line,
    return tuple(return_line)
    # return line,
    
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

def parse_recursive(input_y, input_x, recursion_level, line_X, line_Y):
    global scale_factor, threshhold, read_image
    
    # print input_y, input_x
    
    # store current input
    image_X.append((input_x)/scale_factor)
    image_Y.append((len(read_image) - input_y)/scale_factor)
    
    line_X.append((input_x)/scale_factor)
    line_Y.append((len(read_image) - input_y)/scale_factor)
    
    #erase from image array
    # print input_y, input_x, read_image[input_y][input_x]
    read_image[input_y][input_x] = [1, 1, 1, 1]
    
    x_min = 0
    x_max = len(read_image[0])
    y_min = 0
    y_max = len(read_image)
    # print 'Y',y_min,y_max,'/X',x_min, x_max, "\t", input_y,input_x
    
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
        

parse_image()

# line, = ax.plot([], [], lw=2)

for x_list, y_list in parse_list:
    anim_line, = ax.plot([], [], lw=2)

    line_list.append((x_list, y_list, anim_line))
    
# call the animator.  blit=True means only re-draw the parts that have changed.
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=frames, interval=interval, blit=False)

plt.show()










    
    
    
    
    