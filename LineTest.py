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
ax = plt.axes(xlim=(-2, 2), ylim=(-2, 2))
line, = ax.plot([], [], lw=2)


# global x
# global y

# x = 0.5
# y = 1.0

arm1 = 1.0
arm2 = 1.0

theta1pos= 0.0
theta2pos = 0.0

theta1neg= 0.0
theta2neg = 0.0

intervals = 20


# initialization function: plot the background of each frame
def init():
    line.set_data([], [])
    return line,

# animation function.  This is called sequentially
def animate(i):
    x = 0.5
    y = 1.0
    interval = 20.0
    frames = 40.0
    
    # x0 = (x * i )/interval
    # y0 = (y * i )/interval
    # print x*i
    # print y*i
    x0 = (x * (i+1) )/frames
    y0 = (y * (i+1) )/frames
    print x, y, i+1, frames, arm1, arm2, x0, y0
    # theta2pos = 2.0 * np.arctan(np.sqrt( ((arm1 + arm2)**2 - (x0**2 + y0**2)) / ((x0**2 + y0**2) - (arm1 - arm2)**2) ))
    theta2neg = -2.0 * np.arctan(np.sqrt( ((arm1 + arm2)**2 - (x0**2 + y0**2)) / ((x0**2 + y0**2) - (arm1 - arm2)**2) ))

    # theta1pos = np.arctan2(y0,x0) - np.arctan2(arm2*np.sin(theta2pos), arm1 + arm2 * np.cos(theta2pos))
    theta1neg = np.arctan2(y0,x0) - np.arctan2(arm2*np.sin(theta2neg), arm1 + arm2 * np.cos(theta2neg))

    x1p = arm1 * np.cos(theta1pos)
    y1p = arm1 * np.sin(theta1pos)
    x2p = arm2 * np.cos(theta2pos + theta1pos) + x1p
    y2p = arm2 * np.sin(theta2pos + theta1pos) + y1p

    x1n = arm1 * np.cos(theta1neg)
    y1n = arm1 * np.sin(theta1neg)
    x2n = arm2 * np.cos(theta2neg + theta1neg) + x1n
    y2n = arm2 * np.sin(theta2neg + theta1neg) + y1n

    # print "Positive:\n\t (" , x1p , ", " , y1p , ")\t(" , x2p , ", " , y2p , ")\n"
    print "Negative:\n\t (" , x1n , ", " , y1n , ")\t(" , x2n , ", " , y2n , ")\n"


    # x = np.linspace(0, 2, 10)
    # x = (0, x1p, x2p)
    x = (0, x1n, x2n)
    # y = np.sin(2 * np.pi * (x - 0.01 * i))
    # y = (0, y1p, y2p)
    y = (0, y1n, y2n)
    line.set_data(x, y)
    return line,

# call the animator.  blit=True means only re-draw the parts that have changed.
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=40, interval=intervals, blit=True)

# save the animation as an mp4.  This requires ffmpeg or mencoder to be
# installed.  The extra_args ensure that the x264 codec is used, so that
# the video can be embedded in html5.  You may need to adjust this for
# your system: for more information, see
# http://matplotlib.sourceforge.net/api/animation_api.html
# anim.save('basic_animation.mp4', fps=30, extra_args=['-vcodec', 'libx264'])

plt.show()