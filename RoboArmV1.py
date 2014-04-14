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
max_recursion = 1000  #Maximum length of a continuous line.
frames = 20000            #The total length of time the animation runs for
interval = 0.001             #The interval between animation actions

image_X = []            #Used to store the x-coordinates of each particle
image_Y = []            #Used to store the y-coordinates of each particle

parse_list = []              #data structure to store list of lines that compose the image
line_list = []              #data structure to contain list of line objects in addition to list of lines that compose the image

image_location = 'bernese.png'
# image_location = 'bernese2.png'
# image_location = 'tiny_maze2.png'
# image_location = 'test_image.png'
# image_location = 'test_image3.png'
 
#read the image specified by the global variables
read_image = mpimg.imread(image_location)

# First set up the figure, the axis, and the plot element we want to animate
fig = plt.figure()
ax = plt.axes(xlim=(-1, len(read_image[0])/scale_factor) , ylim=(0,  1+ len(read_image)/scale_factor))

# particles holds the locations of the particles
# particles, = ax.plot([], [], 'bo', ms=particles_size)
line, = ax.plot([], [], lw=2)
# parse_list, = ax.plot([], [], lw=2)

# initialization function: plot the background of each frame
def init():
    
    # line.set_data([], [])
    # particles.set_data([], [])
    
    # line.set_data([], [])
    # particles.set_data([], [])

    return line,
    # return line, particles,
    # return particles,

# animation function.  This is called sequentially
def animate(i):
    global image_X, image_Y
    
    return_line = []
    
    line.set_data(image_X[0:i], image_Y[0:i])
    # print line
    # particles.set_data(image_X, image_Y)
    # particles.set_data(image_X[0:i], image_Y[0:i])
    # particles.set_data(image_X[0:10*i], image_Y[0:10*i])
    # particles.set_markersize(particles_size)
    
    # for x_list, y_list, anim_line in line_list:
        # anim_line.set_data(x_list[0:i], y_list[0:i])
        # return_line.append(anim_line)
    # # for x_list, y_list in parse_list:
        # # line.set_data(x_list[0:i], y_list[0:i])
        
    # return line, return_line
    return line,
    # return particles,
    
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
    # read_image[input_y][input_x] = [0, 0, 0, 0]
    # read_image[input_y][input_x] = [1, 1, 1]
    read_image[input_y][input_x] = [1, 1, 1, 1]
    # print input_y, input_x, read_image[input_y][input_x]
    
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
        

        
# for row in read_image:
    # for element in row:
        # print element
        
# parse_image(image)
parse_image()

count = 1
for x_list, y_list in parse_list:
    anim_line, = ax.plot([], [], lw=2)
    # print anim_line
    line_list.append(
                            (
                                x_list, 
                                y_list, 
                                anim_line
                            )
                           )
    # print count, "\t", x_list, y_list, "\n"
    count += 1
    
# print image_X[0:i], image_Y[0:i]
# print image_X[0:20]
# print image_Y[0:20]
                
# call the animator.  blit=True means only re-draw the parts that have changed.
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=frames, interval=interval, blit=True)

plt.show()










    
    
    
    
    