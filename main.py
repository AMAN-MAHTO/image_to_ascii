# Program To Read video 
# and Extract Frames 
import cv2 
from ascii1 import image_to_ascii
from frame_to_video import generate_video
# Function to extract frames 
def FrameCapture(path): 
      
    # Path to video file 
    vidObj = cv2.VideoCapture(path) 
  
    # Used as counter variable 
    count = 0
  
    # checks whether frames were extracted 
    success = 1
  
    while success: 
        # vidObj object calls read 
        # function extract frames 
        success, image = vidObj.read()
        # Saves the frames with frame-count 
        cv2.imwrite("frame%d.jpg" % count, image)
        image_to_ascii(f'frame{count}.jpg')
        count += 1
    print(count)
    generate_video(count-1)
    

    
  
# Driver Code 
if __name__ == '__main__': 
  
    # Calling the function 
    FrameCapture(input('Video name: ')) 
