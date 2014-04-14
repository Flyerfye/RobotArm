# Drawing an Image
# Issa Beekun, March 2014 

# Sample Image
# __________XXXXXXXX
# _______XXX________XXX
# _____XX______________XX
# ____X__________________X
# ___X______XX______XX____X
# __X_______XX______XX_____X
# __X______________________X
# __X______________________X
# __X____XX___________XX___X
# __X_____X___________X____X
# ___X_____XX_______XX____X
# ____X______XXXXXXX_____X
# _____XX______________XX
# _______XXX________XXX
# __________XXXXXXXX

image = [
 ['_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_' ,'_'   ],
 ['_','_','_','_','_','_','_','_','X','X','X','X','X','X','X','X','_','_','_','_','_','_','_','_' ,'_'   ],
 ['_','_','_','_','_','X','X','X','_','_','_','_','_','_','_','_','X','X','X','_','_','_','_','_' ,'_'   ],
 ['_','_','_','X','X','_','_','_','_','_','_','_','_','_','_','_','_','_','_','X','X','_','_','_' ,'_'   ],
 ['_','_','X','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','X','_','_' ,'_'   ],
 ['_','X','_','_','_','_','X','X','_','_','_','_','_','_','_','_','X','X','_','_','_','_','X','_' ,'_'   ],
 ['X','_','_','_','_','_','X','X','_','_','_','_','_','_','_','_','X','X','_','_','_','_','_','X' ,'_'   ],
 ['X','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','X' ,'_'   ],
 ['X','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','X' ,'_'   ],
 ['X','_','_','_','_','X','X','_','_','_','_','_','_','_','_','_','_','X','X','_','_','_','_','X' ,'_'   ],
 ['X','_','_','_','_','_','X','_','_','_','_','_','_','_','_','_','_','X','_','_','_','_','_','X' ,'_'   ],
 ['_','X','_','_','_','_','_','X','X','_','_','_','_','_','_','X','X','_','_','_','_','_','X','_' ,'_'   ],
 ['_','_','X','_','_','_','_','_','_','X','X','X','X','X','X','_','_','_','_','_','_','X','_','_' ,'_'   ],
 ['_','_','_','X','X','_','_','_','_','_','_','_','_','_','_','_','_','_','_','X','X','_','_','_' ,'_'   ],
 ['_','_','_','_','_','X','X','X','_','_','_','_','_','_','_','_','X','X','X','_','_','_','_','_' ,'_'   ],
 ['_','_','_','_','_','_','_','_','X','X','X','X','X','X','X','X','_','_','_','_','_','_','_','_' ,'_'   ],
 ['_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_'    ]
 ]

# image = [
 # ['_','_','_','_','X','_','_','_','_','_','_','_','X','_','_','_','_','_','_','_','_','_','_','_','_'    ],
 # ['_','_','_','_','_','X','_','_','_','_','_','X','_','_','_','_','_','_','_','_','_','_','_','_','_'    ],
 # ['_','_','_','_','_','_','X','_','_','_','X','_','_','_','_','_','_','_','_','X','X','_','_','_','_'    ],
 # ['_','_','_','_','_','_','_','X','_','X','_','_','_','_','_','_','_','_','_','_','_','X','X','X','_'    ],
 # ['_','_','_','_','_','_','_','_','X','_','_','_','_','_','_','_','_','_','_','_','_','X','_','_','X'    ],
 # ['_','_','_','_','_','_','_','X','_','X','_','_','_','_','_','_','_','_','_','_','X','_','_','_','_'    ],
 # ['_','_','_','_','_','_','X','_','_','_','X','_','_','_','_','_','_','_','_','X','X','_','_','_','_'    ],
 # ['_','_','_','_','_','X','_','_','_','_','_','X','_','_','_','_','_','X','X','_','_','_','_','_','_'    ],
 # ['_','_','_','_','X','_','_','_','_','_','_','_','X','_','_','_','_','_','_','_','_','_','_','_','_'    ]
 # ]
 
scale_factor = 1.0
threshhold = 0.9
max_recursion = 50
frames = 100
interval = 100
# image_location = 'bernese.png'
image_location = 'tiny_maze.png'
 
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


# Need to convert bmp or whatever in an array/matrix/whatever data structure
# Need to figure out the math behind moving the arm

# import numpy as np
# import sys

# arm1 = 1.25
# arm2 = 1.25

# x = 0.5
# y = 1.0
# intervals = 20.0

# pos_neg = 1.0
# # pos_neg = -1.0

# def calc_angles(i):
    # x0 = (x * (i+1) )/intervals
    # y0 = (y * (i+1) )/intervals
    # # print x, y, i+1, intervals, arm1, arm2, x0, y0
    # theta2 = pos_neg * 2.0 * np.arctan(np.sqrt( ((arm1 + arm2)**2 - (x0**2 + y0**2)) / ((x0**2 + y0**2) - (arm1 - arm2)**2) ))

    # theta1 = np.arctan2(y0,x0) - np.arctan2(arm2*np.sin(theta2), arm1 + arm2 * np.cos(theta2))

    # x1 = arm1 * np.cos(theta1)
    # y1 = arm1 * np.sin(theta1)
    # x2 = arm2 * np.cos(theta2 + theta1) + x1
    # y2 = arm2 * np.sin(theta2 + theta1) + y1

    # # print "Positive:\n\t (" , x1 , ", " , y1 , ")\t(" , x2 , ", " , y2 , ")\n"
    
    # return (np.rad2deg(theta1), np.rad2deg(theta2))
    
    
# # value = 0
# # while (value < intervals):
    # # # print value
    # # angles = calc_angles(value)
    # # print angles
    
    # # value += 1

# # row = 0
# # col = 0
    
# # display image in terminal
# print "\n\n"
# for row in image:
    # for value in row:
        # sys.stdout.write(value)
    # print "\n"

# # print image[1][5]
# # image[1][5] = '_'
# # print image[1][5]

"""
Matplotlib Animation Example

author: Jake Vanderplas
email: vanderplas@astro.washington.edu
website: http://jakevdp.github.com
license: BSD
Please feel free to use and modify this, but keep the above information. Thanks!
"""

import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
import matplotlib.image as mpimg

# First set up the figure, the axis, and the plot element we want to animate
fig = plt.figure()
# ax = plt.axes(xlim=(-1, len(image[0])/scale_factor), ylim=(0,  len(image)/scale_factor))
# ax = plt.axes(xlim=(-1, 200), ylim=(0,  300))
ax = plt.axes(xlim=(-1, 65), ylim=(0,  50))

# print  len(image[0]), len(image)

# particles holds the locations of the particles
particles, = ax.plot([], [], 'bo', ms=500)
# partX = []
# partY = []

image_X = []
image_Y = []

# initialization function: plot the background of each frame
def init():
    # line.set_data([], [])
    particles.set_data([], [])
    # return line, particles,
    return particles,

# animation function.  This is called sequentially
def animate(i):
    # global partX, partY
    global image_X, image_Y
    # if i <= 0:
        # partX = []
        # partY = []
        
    # partX.append(0.1 * i)
    # partY.append(0.1 * i)
    
    # print image_X[i], image_Y[i]
    
    particles.set_data(image_X[0:10*i], image_Y[0:10*i])
    # particles.set_data(image_X, image_Y)
    particles.set_markersize(2)
        
    # return line, particles,
    return particles,
    
def parse_image(input_image):
    global scale_factor, threshhold
    
    y_index = 0
    x_index = 0
    recursion_level = 0
    
    # iterate through image array
    while y_index < len(input_image):
        # print row
        x_index = 0
        while x_index < len(input_image[y_index]):
            # print len(input_image[y_index])
            # print x_index, y_index, sum(input_image[y_index][x_index])/3
            
            if sum(input_image[y_index][x_index])/4 <= threshhold:
                # print "found", y_index, x_index
                parse_recursive(input_image,y_index, x_index, recursion_level)
                
                # print "(", ((x_index)/scale_factor), ",",((len(input_image) - y_index)/scale_factor), ")"
                
            x_index += 1
        y_index += 1

def parse_recursive(input_image,input_y, input_x, recursion_level):
    global scale_factor, threshhold
    
    # print input_x, input_y
    
    # store current input
    image_X.append((input_x)/scale_factor)
    image_Y.append((len(input_image) - input_y)/scale_factor)
    
    #erase from image array
    # input_image[input_y][input_x] = '_'
    # print sum(input_image[input_y][input_x])/4
    input_image[input_y][input_x] = [0, 0, 0]
    
    x_min = 0
    x_max = len(input_image[0])
    y_min = 0
    y_max = len(input_image)
    
    if(recursion_level < max_recursion):
        recursion_level += 1
        
        print recursion_level
    
        # print 'Y',y_min,y_max,'/X',x_min, x_max, "\t", input_y,input_x
        # top left
        if input_y > y_min and input_x > x_min and sum(input_image[input_y - 1][input_x - 1])/4 <= threshhold:
            # print "top-left"
            parse_recursive(input_image, input_y - 1, input_x - 1, recursion_level)
        #top
        elif input_y > y_min and sum(input_image[input_y - 1][input_x])/4 <= threshhold:
            # print "top"
            parse_recursive(input_image, input_y - 1, input_x, recursion_level)
        #top right
        elif input_y > y_min and input_x < x_max-1 and sum(input_image[input_y - 1][input_x + 1])/4 <= threshhold:
            # print "top-right"
            parse_recursive(input_image, input_y - 1, input_x + 1, recursion_level)
        # right
        elif input_x < x_max-1 and sum(input_image[input_y][input_x + 1])/4 <= threshhold:
            # print "right"
            parse_recursive(input_image, input_y, input_x + 1, recursion_level)
        # bot right
        elif input_x < x_max-1 and input_y < y_max-1 and sum(input_image[input_y + 1][input_x + 1])/4 <= threshhold:
            # print "bot-right"
            parse_recursive(input_image, input_y + 1, input_x + 1, recursion_level)
        # bot
        elif input_y < y_max-1 and sum(input_image[input_y + 1][input_x])/4 <= threshhold:
            # print "bot"
            parse_recursive(input_image, input_y + 1, input_x, recursion_level)
        # bot left
        elif input_y < y_max-1 and input_x > x_min and sum(input_image[input_y + 1][input_x - 1])/4 <= threshhold:
            # print "bot-left"
            parse_recursive(input_image, input_y + 1, input_x - 1, recursion_level)
        # left
        elif input_x > x_min and sum(input_image[input_y][input_x - 1])/4 <= threshhold:
            # print "left"
            parse_recursive(input_image, input_y, input_x - 1, recursion_level)
        # else:
            # print "none"
        
# read_image = mpimg.imread('sb.png')
read_image = mpimg.imread(image_location)
        
# for row in read_image:
    # for element in row:
        # print element
        
# parse_image(image)
parse_image(read_image)

# print image_X[0:i], image_Y[0:i]
# print image_X[0:20]
# print image_Y[0:20]
                
# call the animator.  blit=True means only re-draw the parts that have changed.
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=frames, interval=interval, blit=True)

plt.show()










    
    
    
    
    