
from matplotlib import pyplot as plt
from matplotlib import animation
import numpy as np

frames = 8            #The total length of time the animation runs for
interval = 2000           #The interval between animation actions
particles_size = 3      #Size of particles displayed
read_image = []         #image passed in to the display function
scale_factor = 1.0      #Scale the image dimensions

arm1 = 100.0             #The length of arm 1 
arm2 = 100.0             #The length of arm 2 

line_list = []          #data structure to contain list of line objects in addition to list of lines that compose the image
parse_list = []         #data structure to store list of lines that compose the image

fig = plt.figure()  

def display_image(input_image = [], input_parse_list = []):
    global read_image, parse_list
    
    if input_image == [] or input_parse_list == []:
        print "No image supplied, using test image"
        test_image()
    else:
        read_image = input_image
        parse_list = input_parse_list
         
#     test_image()
    
    # # call the animator.  blit=True means only re-draw the parts that have changed.
    anim = animation.FuncAnimation(fig, animate, init_func=init,
                                   frames=frames, interval=interval, blit=False)

    plt.show()
 
# initialization function: plot the background of each frame
def init():
    global ax
   
    # First set up the figure, the axis, and the plot element we want to animate
#     ax = plt.axes(xlim=(-1, len(read_image[0])/scale_factor) , ylim=(0,  1+ len(read_image)/scale_factor))
    ax = plt.axes(xlim=(-1, 100) , ylim=(0, 100))

    for x_list, y_list in parse_list:
        anim_line, = ax.plot([], [], lw=2)
                                                                                                         
        line_list.append((x_list, y_list, anim_line))
    
    # line.set_data([], [])
    
    return_line = []
    for x_list, y_list, anim_line in line_list:
        anim_line.set_data(x_list, y_list)
        return_line.append(anim_line)
    
    return tuple(return_line)
    # return line, 

 
# animation function.  This is called sequentially
def animate(i):
    return_line = []
    print i
    for x_list, y_list, anim_line in line_list:
        anim_line.set_data(x_list, y_list)
        return_line.append(anim_line)
        
    return tuple(return_line)
    # return line,

    
def test_image():
    global parse_list, scale_factor
        
    line_X = [0, 10, 10,  0,  0]
    line_Y = [0,  0, 10, 10,  0]
        
    parse_list.append((line_X,line_Y))
    read_image.append((line_X,line_Y))

    return read_image, parse_list
    
    
def simulate_arm(input_angle_list = []):
    global arm_position_list
    if input_angle_list == []:
        print "No angle list supplied"
    else:
        arm_position_list = generate_arm_positions(input_angle_list)
        anim = animation.FuncAnimation(fig, animate_arm, init_func=init_sim,
                                   frames=frames, interval=interval, blit=False)

        plt.show()
        
def generate_arm_positions(input_angle_list = []):
    arm_position_list = []
    
    for theta1, theta2, theta3, xi, yi in input_angle_list:
        theta1 += 90
        x1 = arm1*np.cos(np.radians(theta1))
        y1 = arm1*np.sin(np.radians(theta1))
        xp = arm2*np.cos(np.radians(theta1 + theta2))
        yp = arm2*np.sin(np.radians(theta1 + theta2))
             
        x2 = x1 + xp
        y2 = y1 + yp
        
        arm_position_list.append([[0,x1, x2],[0,y1, y2]])
    
    return arm_position_list
    

# initialization function: plot the background of each frame
def init_sim():
    global ax
   
    # First set up the figure, the axis, and the plot element we want to animate
#     ax = plt.axes(xlim=(-1, len(arm_position_list[0])/scale_factor) , ylim=(0,  1+ len(arm_position_list)/scale_factor))
    ax = plt.axes(xlim=(-100, 100) , ylim=(-100, 100))

    for x_list, y_list in arm_position_list:
        anim_line, = ax.plot([], [], lw=2)
                                                                                                         
        line_list.append((x_list, y_list, anim_line))
    
    # line.set_data([], [])
    
    return_line = []
    for x_list, y_list, anim_line in line_list:
        anim_line.set_data([], [])
        return_line.append(anim_line)
      
    return tuple(return_line)
    # return line, 
    
# animation function.  This is called sequentially
def animate_arm(i):
    return_line = []
    print i
    if i == 0:
        for x_list, y_list, anim_line in line_list:
            anim_line.set_data([], [])
            return_line.append(anim_line)
    else:    
        for x_list, y_list, anim_line in line_list[0:i]:
#             print np.floor(x_list), np.floor(y_list), "\n"
            print x_list, y_list, "\n"
            anim_line.set_data(x_list, y_list)
            return_line.append(anim_line)
              
    return tuple(return_line)
    
if __name__ == "__main__":
    print "This module is intended to supplement the RobotArmV1 script."
    