import cv2
import imutils as im
import time as ti
trivia = [["Which popular Christmas beverage is also called \\“milk punch?\\", "Eggnog"]]


def timeToGo():
    days = 25 - int(ti.strftime('%d'))
    hours = 24 - int(ti.strftime('%H'))
    minutes = 60 - int(ti.strftime('%M'))

    return [days, hours, minutes]

# Reading the image
image = cv2.imread("images/pexels-kristina-paukshtite-3444345.jpg")
image = im.resize(image, width=1080)
# Using cv2.putText()
position = (10, 50)
left = timeToGo()
new_image = cv2.putText(
    image,
    text="Question:",
    org=(10, 200),
    fontFace=cv2.FONT_HERSHEY_DUPLEX,
    fontScale=2.0,
    color=(125, 246, 55),
    thickness=3
)


new_image = cv2.putText(
    image,
    text=trivia[0][0],
    org=(10, 270),
    fontFace=cv2.FONT_HERSHEY_DUPLEX,
    fontScale=2.0,
    color=(125, 246, 55),
    thickness=3
)

new_image = cv2.putText(
    image,
    text="Answer",
    org=(10, 540),
    fontFace=cv2.FONT_HERSHEY_DUPLEX,
    fontScale=2.0,
    color=(125, 246, 55),
    thickness=3
)

new_image = cv2.putText(
    image,
    text=trivia[0][1],
    org=(10, 540),
    fontFace=cv2.FONT_HERSHEY_DUPLEX,
    fontScale=2.0,
    color=(125, 246, 55),
    thickness=3
)

# Saving the new image
cv2.imshow("MyImage", image)
# cv2.imwrite("NewWallpaper.jpg", new_image)
cv2.waitKey(0)