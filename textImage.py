# # Python program to explain cv2.putText() method
#
# # importing cv2
# import cv2
#
# # path
# path = r'C:\Users\philo\PycharmProjects\openCvTest\images\pexels-kristina-paukshtite-3444345.jpg'
#
# # Reading an image in default mode
# image = cv2.imread(path)
#
# # Window name in which image is displayed
# window_name = 'Image'
#
# # font
# font = cv2.FONT_HERSHEY_SIMPLEX
#
# # org
# org = (50, 50)
#
# # fontScale
# fontScale = 1
#
# # Blue color in BGR
# color = (255, 0, 0)
#
# # Line thickness of 2 px
# thickness = 2
#
# # Using cv2.putText() method
# image = cv2.putText(image, 'OpenCV', org, font,
#                     fontScale, color, thickness, cv2.LINE_AA)
#
# # Displaying the image
# cv2.imshow(window_name, image)

# importing cv2 library
import cv2
import imutils as im
import time as ti


def timeToGo():
    days = 25 - int(ti.strftime('%d'))
    hours = 24 - int(ti.strftime('%H'))
    minutes = 60 - int(ti.strftime('%M'))

    return [days, hours, minutes]

# Reading the image
image = cv2.imread("images/pexels-kristina-paukshtite-3444345.jpg")
image = im.resize(image, width=800)
# Using cv2.putText()
position = (10, 50)
left = timeToGo()
new_image = cv2.putText(
    image,
    text="Days: Hours: Minutes:",
    org=(10, 200),
    fontFace=cv2.FONT_HERSHEY_DUPLEX,
    fontScale=2.0,
    color=(125, 246, 55),
    thickness=3
)

timeStr = "  {}     {}      {}".format(left[0], left[1], left[2])

new_image = cv2.putText(
    image,
    text=timeStr,
    org=(10, 270),
    fontFace=cv2.FONT_HERSHEY_DUPLEX,
    fontScale=2.0,
    color=(125, 246, 55),
    thickness=3
)

# Saving the new image
cv2.namedWindow("MyImage", cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty("MyImage",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
cv2.imshow("MyImage", image)
# cv2.imwrite("NewWallpaper.jpg", new_image)
cv2.waitKey(0)
print(timeToGo())

# cv2.namedWindow("window", cv2.WND_PROP_FULLSCREEN)
# cv2.setWindowProperty("window",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
# cv2.imshow("window", img)

