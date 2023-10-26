from ImagePreprocess import *
import cv2
from tkinter import filedialog 
from tkinter import *
import time

# START PATH SELECTION (ONLY USE IN PLACE OF VIDEO INPUT)
#--------------------------------------------------------
# Destroy root window (used for selecting files)
root = Tk()
root.withdraw()

# Select file name and cleanse it
#path = filedialog.askopenfile().name
#path = path.replace("/", "//")
#-------------------------------------------------------

video = cv2.VideoCapture(0) # Defines camera input
#video = cv2.VideoCapture(path)

prev_frame_time = 0
new_frame_time = 0
font = cv2.FONT_HERSHEY_SIMPLEX

# Define desired frame rate (loop control)
ctrl_FPS = 30

while(True):
    ret, frame = video.read()

    # Quit Command : q
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    new_frame_time = time.time()

    # Capture grayscale image
    new_frame = imagePreprocess(frame)

    # Useful statistics
    org_width = video.get(cv2.CAP_PROP_FRAME_WIDTH)
    org_height = video.get(cv2.CAP_PROP_FRAME_HEIGHT)
    new_width = new_frame.shape[1]
    new_height = new_frame.shape[0]

    fps = 1 / (new_frame_time - prev_frame_time)
    prev_frame_time = new_frame_time
    fps_str = str(int(fps))

    #Print stats onto image
    cv2.putText(frame, "Shape (WxH): " + str(org_width) + ", " + str(org_height),
                (7, 20), font, 0.5, (255, 255, 255), 1, cv2.LINE_AA) 
    cv2.putText(frame, "FPS: " + fps_str, (7, 40), font, 0.5, (255, 255, 255), 1, cv2.LINE_AA) 
    cv2.putText(new_frame, "Shape (WxH): " + str(new_width) + ", " + str(new_height),
                (7, 20), font, 0.5, (255, 255, 255), 1, cv2.LINE_AA) 
    cv2.putText(new_frame, "FPS: " + fps_str, (7, 40), font, 0.5, (255, 255, 255), 1, cv2.LINE_AA)     
    
    
    # Shows standard camera view
    cv2.imshow('Original Input', frame)
    cv2.imshow('Processed Input', new_frame)

    # Control framerate within the while loop
    time.sleep(max(1./ctrl_FPS - (1 / fps), 0))

    

video.release()
cv2.destroyAllWindows()
