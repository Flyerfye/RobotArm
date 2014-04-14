# Drawing an Image
# Issa Beekun, March 2014 

# Sample Image
         # XXXXXXXXX
      # XXX          XXX
    # XX                  XX  
   # X                        X  
  # X      XX      XX     X  
 # X       XX      XX      X  
 # X                           X  
 # X                           X  
 # X    XX           XX    X  
 # X     X             X     X  
  # X     XX       XX     X  
   # X     XXXXXX      X  
    # XX                 XX      
      # XXX         XXX          
         # XXXXXXX
 
 
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
