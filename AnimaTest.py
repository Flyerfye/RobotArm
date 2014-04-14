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
ax = plt.axes(xlim=(0, 2), ylim=(-2, 2))
# line, = ax.plot([], [], lw=2)

# particles holds the locations of the particles
particles, = ax.plot([], [], 'bo', ms=6)
partX = []
partY = []

# initialization function: plot the background of each frame
def init():
    # line.set_data([], [])
    particles.set_data([], [])
    # return line, particles,
    return particles,

# animation function.  This is called sequentially
def animate(i):
    global partX, partY
    if i <= 0:
        partX = []
        partY = []
        print "Reset", partX, partY
    
    # x = np.linspace(0, 2, 1000)
    # y = np.sin(2 * np.pi * (x - 0.01 * i))
    # line.set_data(x, y)
    partX.append(0.1 * i)
    partY.append(0.1 * i)
    
    particles.set_data(partX, partY)
    particles.set_markersize(5)
    
    print i
    
    # return line, particles,
    return particles,

# call the animator.  blit=True means only re-draw the parts that have changed.
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=20, interval=5, blit=True)

# save the animation as an mp4.  This requires ffmpeg or mencoder to be
# installed.  The extra_args ensure that the x264 codec is used, so that
# the video can be embedded in html5.  You may need to adjust this for
# your system: for more information, see
# http://matplotlib.sourceforge.net/api/animation_api.html
# anim.save('basic_animation.mp4', fps=30, extra_args=['-vcodec', 'libx264'])

plt.show()



# x = 1 
# y = 1

# arm1 = 1
# arm2 = 1

# theta1pos= 0
# theta2pos = 0

# theta1neg= 0
# theta2neg = 0

# theta2pos = 2 * arctan(sqrt( ((arm1 + arm2)**2 - (x**2 + y**2)) / ((x**2 + y**2) - (arm1 - arm2)**2) ))
# theta2neg = -2 * arctan(sqrt( ((arm1 + arm2)**2 - (x**2 + y**2)) / ((x**2 + y**2) - (arm1 - arm2)**2) ))

# theta1pos = arctan2(y,x) - arctan2(arm2*sin(theta2pos), arm1 + arm2 cos(theta2pos))
# theta1neg = arctan2(y,x) - arctan2(arm2*sin(theta2neg), arm1 + arm2 cos(theta2neg))

# x1p = arm1 * cos(theta1pos)
# y1p = arm1 * sin(theta1pos)
# x2p = arm2 * cos(theta2pos) + x1p
# y2p = arm2 * sin(theta2pos) + y1p

# x1n = arm1 * cos(theta1neg)
# y1n = arm1 * sin(theta1neg)
# x2n = arm2 * cos(theta2neg) + x1n
# y2n = arm2 * sin(theta2neg) + y1n

# print "Positive:\n\t (x1p, y1p)\t(x2p, y2p)\n"
# print "Negative:\n\t (x1n, y1n)\t(x2n, y2n)\n"
































