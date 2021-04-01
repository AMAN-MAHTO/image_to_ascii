import os 
import cv2  
from PIL import Image  
  
# Video Generating function 
def generate_video(no_of_images): 
    image_folder = 'C:\\Users\\ashok mahato\\Desktop\\programing\\files\\Python_learning\\image_to_ascii' # make sure to use your folder 
    video_name = f'{no_of_images}.mp4'
    images=[]
    for i in range(no_of_images):
        images.append(f'frame{i}.png')
    
    # Array images should only consider 
    # the image files ignoring others if any   
  
    frame = cv2.imread(os.path.join(image_folder, images[0])) 
    # setting the frame width, height width 
    # the width, height of first image 
    height, width, layers = frame.shape   
  
    video = cv2.VideoWriter(video_name, 0, 22, (width, height))  
  
    # Appending the images to the video one by one 
    for image in images:  
        video.write(cv2.imread(os.path.join(image_folder, image))) 
    
    for i in images:
        os.remove(i)
    # Deallocating memories taken for window creation 
    cv2.destroyAllWindows()  
    video.release()  # releasing the video generated 
  
  
# Calling the generate_video function
generate_video(901)

