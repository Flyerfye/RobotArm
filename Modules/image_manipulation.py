
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
                
                parse_recursive(y_index, x_index, recursion_level, line_X, line_Y, input_direction=1)
                parse_list.append((line_X,line_Y))
                
                # print "Finished Line\n"
            x_index += 1
        y_index += 1
        
    return read_image, parse_list

# recursively determine if the points surrounding the current point should be added to current line
# uses a pre-defined thresh hold limit

def parse_recursive(input_y, input_x, recursion_level, line_X, line_Y, input_direction):    
    # store current input
    # if(np.sqrt((input_x - dX)**2 + (input_y - dY)**2)>dT) or (recursion_level==0):
    
    #if current point is first point, add this point
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
        
        #keeps track of how many directions have been checked, breaking when > 8
        directions_checked = 0
        
        #keeps track of current direction
        current_direction = input_direction
        
        #keeps track of whether the next point has been found
        point_found = False
             
        while(directions_checked <= 8 and point_found==False):
            if(check_dict[current_direction](input_x, input_y)):
                #if the line changes direction, add that corner point
                if(current_direction!=input_direction):
                    line_X.append((input_x)/scale_factor)
                    line_Y.append((len(read_image) - input_y)/scale_factor)
                    
                point_found = True
                move_dict[current_direction](input_x, input_y, recursion_level, line_X, line_Y, current_direction)
            else:
                #increment the number of directions checked as well as the next direction to check
                directions_checked += 1
                
                if(current_direction < 8):
                    current_direction += 1
                else:
                    current_direction = 1
        
        #if the current point is last point, add the final point
        if(point_found==False):
            line_X.append((input_x)/scale_factor)
            line_Y.append((len(read_image) - input_y)/scale_factor)
        
#         # print recursion_level
#         if check_right(input_x, input_y):
#             move_right(input_x, input_y, recursion_level, line_X, line_Y, curr_direction)
#         else:
#             # store current input
#             line_X.append((input_x)/scale_factor)
#             line_Y.append((len(read_image) - input_y)/scale_factor)

    return True

def check_right(input_x, input_y):
    return (True if input_x < x_max-1 and sum(read_image[input_y][input_x + 1])/4 <= threshhold else False)    

def check_bot_right(input_x, input_y):
    return (True if input_x < x_max-1 and input_y < y_max-1 and sum(read_image[input_y + 1][input_x + 1])/4 <= threshhold else False)      

def check_bot(input_x, input_y):
    return (True if input_y < y_max-1 and sum(read_image[input_y + 1][input_x])/4 <= threshhold else False)       

def check_bot_left(input_x, input_y):
    return (True if input_y < y_max-1 and input_x > x_min and sum(read_image[input_y + 1][input_x - 1])/4 <= threshhold else False)       

def check_left(input_x, input_y):
    return (True if input_x > x_min and sum(read_image[input_y][input_x - 1])/4 <= threshhold else False)    

def check_top_left(input_x, input_y):
    return (True if input_y > y_min and input_x > x_min and sum(read_image[input_y - 1][input_x - 1])/4 <= threshhold else False)

def check_top(input_x, input_y):
    return (True if input_y > y_min and sum(read_image[input_y - 1][input_x])/4 <= threshhold else False)    

def check_top_right(input_x, input_y):
    return (True if input_y > y_min and input_x < x_max-1 and sum(read_image[input_y - 1][input_x + 1])/4 <= threshhold else False)    

def move_right(input_x, input_y, recursion_level, line_X, line_Y, current_direction):
    return parse_recursive(input_y, input_x + 1, recursion_level, line_X, line_Y, current_direction)

def move_bot_right(input_x, input_y, recursion_level, line_X, line_Y, current_direction):
    return parse_recursive(input_y + 1, input_x + 1, recursion_level, line_X, line_Y, current_direction)   

def move_bot(input_x, input_y, recursion_level, line_X, line_Y, current_direction):
    return parse_recursive(input_y + 1, input_x, recursion_level, line_X, line_Y, current_direction)

def move_bot_left(input_x, input_y, recursion_level, line_X, line_Y, current_direction):
    return parse_recursive(input_y + 1, input_x - 1, recursion_level, line_X, line_Y, current_direction)    

def move_left(input_x, input_y, recursion_level, line_X, line_Y, current_direction):
    return parse_recursive(input_y, input_x - 1, recursion_level, line_X, line_Y, current_direction)

def move_top_left(input_x, input_y, recursion_level, line_X, line_Y, current_direction):
    return parse_recursive(input_y - 1, input_x - 1, recursion_level, line_X, line_Y, current_direction)

def move_top(input_x, input_y, recursion_level, line_X, line_Y, current_direction):
    return parse_recursive(input_y - 1, input_x, recursion_level, line_X, line_Y, current_direction)

def move_top_right(input_x, input_y, recursion_level, line_X, line_Y, current_direction):
    return parse_recursive(input_y - 1, input_x + 1, recursion_level, line_X, line_Y, current_direction)

check_dict = {
              #direction number: corresponding function
              #function call:
              #    check_dict[direction number](input_x, input_y)
              1: check_right,
              2: check_bot_right,
              3: check_bot,
              4: check_bot_left,
              5: check_left,
              6: check_top_left,
              7: check_top,
              8: check_top_right,
          }

move_dict = {
              #direction number: corresponding function
              #function call:
              #    move_dict[direction number](input_x, input_y, recursion_level, line_X, line_Y)
              1: move_right,
              2: move_bot_right,
              3: move_bot,
              4: move_bot_left,
              5: move_left,
              6: move_top_left,
              7: move_top,
              8: move_top_right,
          }

if __name__ == "__main__":
    print "This module is intended to suplement the RobotArmV1 script."
    
    