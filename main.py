import cv2
import os
import random
import time as ti
import numpy as np

videoFile = []
windowName = "vidow"
startTime = 17.30
endTime = 22.30


"""
Source https://stackoverflow.com/questions/3964681/find-all-files-in-a-directory-with-extension-txt-in-python
Anaswer by ghostdog74
"""

for file in os.listdir(os.getcwd() + "\\video"):
    if file.endswith(".mp4"):
        videoFile.append(file)
print(videoFile)


# Create a VideoCapture object and read from input file
cap = cv2.VideoCapture(videoFile[random.randrange(0, len(videoFile), 1)])

# Check if camera opened successfully
if (cap.isOpened() == False):
    print("Error opening video  file")


cv2.namedWindow(windowName, cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty(windowName, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
# Read until video is completed
while (cap.isOpened()):

    # Capture frame-by-frame
    ret, frame = cap.read()
    if ret == True:

        # Display the resulting frame
        cv2.imshow(windowName, frame)

        # Press Q on keyboard to  exit
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    # Break the loop
    else:
        break

# When everything done, release
# the video capture object
cap.release()

# Closes all the frames
cv2.destroyAllWindows()


def days_on():
    if 22.30 < float(ti.strftime('%H')) + float(ti.strftime('%M')) > 17.29:
        print("In time range")
    else:
        print("Too late or early")

