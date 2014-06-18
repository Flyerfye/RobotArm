import numpy as np

rad2deg = 180/np.pi

# pen_down  = np.radians(60)     #angle when pen is down
# pen_up = np.radians(150)                  #angle when pen is up
pen_down  = 60    #angle when pen is down
pen_up = 150                  #angle when pen is up

theta1_min = 0
theta1_max = 180
theta2_min = 0
theta2_max = 145
theta3_min = 60
theta3_max = 150

arm1 = 57.1             #The length of arm 1 
arm2 = 57.1              #The length of arm 2 

angle_list = []           #data structure to store servo angles for robotic arm


def get_angles(Pxi, Pyi):
    global arm1, arm2
    
    Pxf = 0
    Pyf = 0
        
        
    # rotate each point 90 degrees (pi/2) to accommodate the drawing capabilities of the arm
    sin_value = np.sin(np.pi/2);
    cos_value = np.cos(np.pi/2);
    
    # translate point back to origin:
    Pxf -= Pxi;
    Pyf -= Pyi;
    
    xnew = Pxf * cos_value + Pyf * sin_value;
    ynew = -Pxf * sin_value + Pyf * cos_value;
    
    # translate point back:
    Pxf = xnew + Pxi;
    Pyf = ynew + Pyi;
  
#     offset to compensate for arm equations assuming unlimited rotational freedom of arm servos
#     Pxf += arm1 + arm2
#     Pxf += 20
#     Pyf += 20
#     Pxf = -Pxf
#     Pyf = -Pyf

    # first find theta2 where c2 = cos(theta2) and s2 = sin(theta2)
    c2 = (Pxf**2 + Pyf**2 - arm1**2 - arm2**2)/(2*arm1*arm2) #is btwn -1 and 1
#     print c2
    s2 = np.sqrt(1 - c2**2) #sqrt can be + or -, and each corresponds to a different orientation
    theta2 = np.degrees(np.arctan2(s2,c2)) #- 34.56 # solves for the angle in degrees and places in correct quadrant
    theta1 = np.degrees(np.arctan2(-arm2*s2*Pxf + (arm1 + arm2*c2)*Pyf, (arm1 + arm2*c2)*Pxf + arm2*s2*Pyf))

    return theta1, theta2

# takes as input the parse_list containing lines that compose the parsed image
# generates a list of angles for the three servos of the robot arm
def generate_arm_angles(parse_list):
    global pen_up, pen_down, angle_list

    #makes sure the angle list is empty before beginning
#     angle_list = []
    del angle_list
    angle_list = []
    
    # angle_list
    for x_list, y_list in parse_list:
        x_init = x_list[0]
        y_init = y_list[0]
        
        theta1_final = 0
        theta2_final = 0
        x_final = 0
        y_final = 0
        
        index = 0
        
        
        #initially, pen is over first point but does not touch it (such a tease)
        theta3pos = pen_up
        theta1pos, theta2pos = get_angles(x_init, y_init)
        # theta2pos = np.arccos((arm1**2 + arm2**2 - (x_init**2 + y_init**2)) / (2*arm1*arm2))
        # theta1pos = np.arctan2(y_init,x_init) - np.arctan2(arm2*np.sin(theta2pos), arm1 + arm2 * np.cos(theta2pos))

        append_angle(theta1pos,theta2pos,theta3pos, x_init, y_init)
                
        while index < len(y_list):
#             print ("X Coord: %.2f\tY Coord: %.2f") % (x_list[index], y_list[index])
            
            theta3pos = pen_down
            theta1pos, theta2pos = get_angles(x_list[index], y_list[index])
            # theta2pos = 2.0 * np.arctan(np.sqrt( ((arm1 + arm2)**2 - (x_list[index]**2 + y_list[index]**2)) / ((x_list[index]**2 + y_list[index]**2) - (arm1 - arm2)**2) ))
            # theta2pos = np.arccos((arm1**2 + arm2**2 - (x_init**2 + y_init**2)) / (2*arm1*arm2))
            # theta1pos = np.arctan2(y_list[index],x_list[index]) - np.arctan2(arm2*np.sin(theta2pos), arm1 + arm2 * np.cos(theta2pos))            
            
            theta2_final = theta2pos
            theta1_final = theta1pos
            x_final = x_list[index]
            y_final = y_list[index]
            
            append_angle(theta1pos,theta2pos,theta3pos,x_list[index], y_list[index])
            
            index += 1
                
        append_angle(theta1_final,theta2_final,pen_up,x_final,y_final)
        
    return angle_list

def append_angle(theta1 = -1, theta2 = -1, theta3 = -1, x=-1, y=-1):
    if(theta1 < theta1_min or theta1 > theta1_max):
        print "Theta1 value is out of bounds: " + str(theta1_min) + " <? " + str(theta1) + " <? " + str(theta1_max)  
        
    if(theta2 < theta2_min or theta2 > theta2_max):
        print "Theta2 value is out of bounds: " + str(theta2_min) + " <? " + str(theta2) + " <? " + str(theta2_max)  
        
    if(theta3 < theta3_min or theta3 > theta3_max):
        print "Theta3 value is out of bounds: " + str(theta3_min) + " <? " + str(theta3) + " <? " + str(theta3_max)  
        
    theta1 = (np.floor(1 * theta1 * 100) / 100) #+ 90
    theta2 = (np.floor(1 * theta2 * 100) / 100) 
    theta3 = (np.floor(rad2deg * theta3 * 100) / 100)    
    
    angle_list.append([theta1,theta2,theta3,x,y])
    
def write_angle(theta_selection = 'Z', angle = -1.0, serial_connection=''):
    if ((theta_selection is 'A') or (theta_selection is 'B') or (theta_selection is 'C')):
        output_string = ''
        
        output_string += '['
        output_string += theta_selection
        output_string += "%.2f" % angle
        output_string += ']'
        
        
        
        # raw_input(output_string)
        
        # print output_string
        serial_connection.write(output_string)

        input_character = serial_connection.read()
        # print input_character
        
        # loop until arduino signals it has finished reading current angle value
        while input_character != 'X':
            input_character = serial_connection.read()        
            # print input_character
            
        # print input_character
    else:
        return
    
    
if __name__ == "__main__":
    print "This module is intended to suplement the RobotArmV1 script."