import cv2
import random
import file_access as fa


class DisplayVideo:

    def __init__(self):
        self.video_list = fa.FileAccess().get_video_files()

    def play_video(self):
        window_name = "video"
        # Create a VideoCapture object and read from input file
        cap = cv2.VideoCapture(self.video_list[random.randrange(0, len(self.video_list), 1)])

        # Check if camera opened successfully
        if not cap.isOpened():
            print("Error opening video  file")

        cv2.namedWindow(window_name, cv2.WND_PROP_FULLSCREEN)
        cv2.setWindowProperty(window_name, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        # Read until video is completed
        while cap.isOpened():

            # Capture frame-by-frame
            ret, frame = cap.read()
            if ret:

                # Display the resulting frame
                cv2.imshow(window_name, frame)

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
