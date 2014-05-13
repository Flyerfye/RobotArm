
from matplotlib import pyplot as plt
from matplotlib import animation

frames = 300             #The total length of time the animation runs for
interval = 1                #The interval between animation actions
particles_size = 3      #Size of particles displayed
read_image = []   #image passed in to the display function
scale_factor = 1.0     #Scale the image dimensions

line_list = []              #data structure to contain list of line objects in addition to list of lines that compose the image
parse_list = []           #data structure to store list of lines that compose the image
  

def display_image(input_image = [], input_parse_list = []):
    global read_image, parse_list
    
    # if input_image == [] or input_parse_list == []:
        # print "No image supplied, using test image"
        # test_image()
    # else:
        # read_image = input_image
        # parse_list = input_parse_list
        
    test_image()
    
    # # call the animator.  blit=True means only re-draw the parts that have changed.
    anim = animation.FuncAnimation(fig, animate, init_func=init,
                                   frames=frames, interval=interval, blit=False)

    plt.show()
 
 
# initialization function: plot the background of each frame
def init():
    global ax
   
    # First set up the figure, the axis, and the plot element we want to animate
    ax = plt.axes(xlim=(-1, len(read_image[0])/scale_factor) , ylim=(0,  1+ len(read_image)/scale_factor))

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
    
    for x_list, y_list, anim_line in line_list:
        anim_line.set_data(x_list[0:i], y_list[0:i])
        return_line.append(anim_line)
        
    return tuple(return_line)
    # return line,
    
    
fig = plt.figure()
    
def test_image():
    global parse_list, scale_factor
    
    line_X = [10,20,20,10,10]
    line_Y = [10,10,20,20,10]
        
    parse_list.append((line_X,line_Y))
    read_image.append((line_X,line_Y))

    
if __name__ == "__main__":
    print "This module is intended to suplement the RobotArmV1 script."
    