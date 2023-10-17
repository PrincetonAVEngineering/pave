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
# path = filedialog.askopenfile().name
# path = path.replace("/", "//")
#-------------------------------------------------------

video = cv2.VideoCapture(0) # Defines camera input
# video = cv2.VideoCapture(path)

prev_frame_time = 0
new_frame_time = 0
font = cv2.FONT_HERSHEY_SIMPLEX

while(True):
    ret, frame = video.read()

    # Quit Command : q
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    new_frame_time = time.time()

    # Capture grayscale image
    new_frame = imagePreprocess(frame)

    # Useful statistics
    width = video.get(cv2.CAP_PROP_FRAME_WIDTH)
    height = video.get(cv2.CAP_PROP_FRAME_HEIGHT)

    fps = 1 / (new_frame_time - prev_frame_time)
    prev_frame_time = new_frame_time
    fps = str(int(fps))

    #Print stats onto image
    cv2.putText(new_frame, "Shape (WxH): " + str(width) + ", " + str(height),
                (7, 20), font, 0.5, (255, 255, 255), 1, cv2.LINE_AA) 
    cv2.putText(new_frame, "FPS: " + fps, (7, 40), font, 0.5, (255, 255, 255), 1, cv2.LINE_AA) 
    
    # Shows standard camera view
    cv2.imshow('Original Input', frame)
    cv2.imshow('Processed Input', new_frame)

    

video.release()
cv2.destroyAllWindows()
