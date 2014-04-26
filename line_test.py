# # import matplotlib libary
# import matplotlib.pyplot as plt
# import numpy as np

# calc_x = (50+3)*(8.0/15)
# calc_y = -3

# print calc_x

# # define some data
# x = [-calc_x, calc_x]
# y = [calc_y, calc_y]

# # plot data
# plt.plot(x, y)

# # show plot
# plt.show()

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

# First set up the figure, the axis, and the plot element we want to animate
fig = plt.figure()
ax = plt.axes(xlim=(-100, 100), ylim=(-100, 100))
line, = ax.plot([], [], lw=2)

arm1 = 100.0
arm2 = 100.0

theta1pos= 0.0
theta2pos = 0.0

# global point_counter
point_counter = 1

points = []

points.append((10, 10))
points.append((10, 20))
points.append((20, 20))
points.append((20, 10))
points.append((10, 10))
# points.append((10, 10))
intervals =100
frames = 10

# initialization function: plot the background of each frame
def init():
    line.set_data([], [])
    return line,

# animation function.  This is called sequentially
def animate(i):
    # global frames, points
    global point_counter
        
    xi, yi = points[point_counter - 1]    
    x, y = points[point_counter]
    
    # interval = 4.0
    # frames = 4.0
    
    # if i == 50:
    # raw_input("Press any for Next.")
    
    # x0 = (x * i )/interval
    # y0 = (y * i )/interval
    # print x*i
    # print y*i
    x0 = (x - xi) * (i)/frames + xi
    y0 = (y - yi) * (i)/frames + yi
    # print x, y, i+1, frames, arm1, arm2, x0, y0
    theta2pos = 2.0 * np.arctan(np.sqrt( ((arm1 + arm2)**2 - (x0**2 + y0**2)) / ((x0**2 + y0**2) - (arm1 - arm2)**2) ))

    theta1pos = np.arctan2(y0,x0) - np.arctan2(arm2*np.sin(theta2pos), arm1 + arm2 * np.cos(theta2pos))

    x1p = arm1 * np.cos(theta1pos)
    y1p = arm1 * np.sin(theta1pos)
    x2p = arm2 * np.cos(theta2pos + theta1pos) + x1p
    y2p = arm2 * np.sin(theta2pos + theta1pos) + y1p
    
    print "Positive(", i,"): start[", xi,",", yi,"]->current[", x0,",", y0,"]->delta[", x,",", y,"] \n\t (" , x1p , ", " , y1p , ")\t(" , x2p , ", " , y2p , ")\n"


    
    if i >= frames - 1:
        # global point_counter
        # global point_counter
        point_counter += 1
        print point_counter
        
        if point_counter >= len(points):
            point_counter = 1
    
    # x = np.linspace(0, 2, 10)
    x = (0, x1p, x2p)
    # y = np.sin(2 * np.pi * (x - 0.01 * i))
    y = (0, y1p, y2p)
    line.set_data(x, y)
        
    
    return line,
    
def thetafn(x0 = 0, y0 = 0):
    theta2pos = 2.0 * np.arctan(np.sqrt( ((arm1 + arm2)**2 - (x0**2 + y0**2)) / ((x0**2 + y0**2) - (arm1 - arm2)**2) )) 
    
        
    theta1pos = np.arctan2(y0,x0) - np.arctan2(arm2*np.sin(theta2pos), arm1 + arm2 * np.cos(theta2pos))
    # theta1pos += np.pi/2
    
    if theta2pos < 0:
        theta2pos += 2*np.pi

    x1p = arm1 * np.cos(theta1pos)
    y1p = arm1 * np.sin(theta1pos)
    x2p = arm2 * np.cos(theta2pos + theta1pos) + x1p
    y2p = arm2 * np.sin(theta2pos + theta1pos) + y1p

    rad2pi = 180/np.pi
    print "P:\t",rad2pi*theta1pos,"(" , x1p , ", " , y1p , ")\n\t",rad2pi*theta2pos,"(" , x2p , ", " , y2p , ")\n"

    
# thetafn(1,0)
# thetafn(1,1)
# thetafn(1,2)
# thetafn(2,1)
# thetafn(2,0)
# call the animator.  blit=True means only re-draw the parts that have changed.
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=frames, interval=intervals, blit=True)

# save the animation as an mp4.  This requires ffmpeg or mencoder to be
# installed.  The extra_args ensure that the x264 codec is used, so that
# the video can be embedded in html5.  You may need to adjust this for
# your system: for more information, see
# http://matplotlib.sourceforge.net/api/animation_api.html
# anim.save('basic_animation.mp4', fps=30, extra_args=['-vcodec', 'libx264'])

plt.show()