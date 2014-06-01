
import numpy as np
import matplotlib.image as mpimg

max_recursion = 300 #Maximum length of a continuous line.
threshhold = 0.5    #Threshold brightness value, determines which points to print. 
                    #Higher value means lighter colors are printed.
scale_factor = 1.0  #Scale the image dimensions
dX = -1.0
dY = -1.0
dT = 0.5
    
x_min = 0
x_max = 0
y_min = 0
y_max = 0


parse_list = []     #data structure to store list of lines that compose the image
                                  
# parses a pre-defined image into a list of lines as defined by x, y groupings
# (the x-coordinates are stored on a list and the y coordinates are stored on a separate list)
def parse_image(image_location):
#     global scale_factor, threshhold, dX, dY, dT, read_image, x_min, x_max, y_min, y_max
    global read_image, x_min, x_max, y_min, y_max
    
    read_image = mpimg.imread(image_location)
    
    y_index = 0
    x_index = 0
    recursion_level = 0
    
    x_min = 0
    x_max = len(read_image[0])
    y_min = 0
    y_max = len(read_image)
    
    # iterate through image array
    while y_index < len(read_image):
        # print row
        x_index = 0
        while x_index < len(read_image[y_index]):

            if (sum(read_image[y_index][x_index])/4 <= threshhold): #\
                # checks to see if current point to plotted is a minimum distance from previous plotted point
                # (np.sqrt((x_index - dX)**2 + (y_index - dY)**2)>dT):  
                line_X = []
                line_Y = []
                dX = x_index
                dY = y_index
                
                parse_recursive(y_index, x_index, recursion_level, line_X, line_Y)
                parse_list.append((line_X,line_Y))
                
                # print "Finished Line\n"
            x_index += 1
        y_index += 1
        
    return read_image, parse_list

# recursively determine if the points surrounding the current point should be added to current line
# uses a pre-defined thresh hold limit

def parse_recursive(input_y, input_x, recursion_level, line_X, line_Y):    
    # store current input
    # if(np.sqrt((input_x - dX)**2 + (input_y - dY)**2)>dT) or (recursion_level==0):
    if(recursion_level==0):
        # store current input
        line_X.append((input_x)/scale_factor)
        line_Y.append((len(read_image) - input_y)/scale_factor)
        
#         dX = input_x
#         dY = input_y
    
    #erase from image array
    read_image[input_y][input_x] = [1, 1, 1, 1]
    
    if(recursion_level < max_recursion):
        recursion_level += 1
        
        # Starts in the upper left corner
        # Searches left to right, top to bottom
        # When it finds the first point to draw, starts heading right
        #     Will continue heading right until no longer able
        #     Starts searching clockwise for next point
        #     When next point is found, will continue in that direction until no longer able 
        #     
        #     
        #     
     
        # print recursion_level
#         if input_x < x_max-1 and sum(read_image[input_y][input_x + 1])/4 <= threshhold:
        if check_right(input_x, input_y):
            # print "right"
            parse_recursive(input_y, input_x + 1, recursion_level, line_X, line_Y)
        else:
            # store current input
            line_X.append((input_x)/scale_factor)
            line_Y.append((len(read_image) - input_y)/scale_factor)

def check_right(input_x, input_y):
    return (True if input_x < x_max-1 and sum(read_image[input_y][input_x + 1])/4 <= threshhold else False)    

if __name__ == "__main__":
    print "This module is intended to suplement the RobotArmV1 script."
    
    