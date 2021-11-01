import cv2
import time as ti
import datetime as dt
import file_access as fa
from random import randrange as rr


class Timer:

    def __init__(self):
        self.file_access = fa.FileAccess()
        self.image_list = self.file_access.get_images_files()
        self.image_path = self.file_access.images_path
        self.current_year = int(ti.strftime('%Y'))
        self.current_month = int(ti.strftime('%m'))
        self.current_day = int(ti.strftime('%d'))
        self.christmas_text = ["Yeah it is Christmas Today", "IT IS CHRISTMAS", "Oh Joy its Christmas"]
        self.image_font = cv2.cv2.FONT_HERSHEY_DUPLEX
        self.image = None

    @property
    def next_christmas(self):
        """
        Tests what the date of next Christmas will be. Returns a Datetime object for next Christmas
        :return: Datetime
        """
        if self.current_month == 12 and self.current_day < 25:
            return dt.datetime(self.current_year + 1, 12, 25, 0)
        else:
            return dt.datetime(self.current_year, 12, 25, 0)

    @property
    def random_image(self):
        """
        Randomly selects a image file from the self.image_list
        (List of Strings for the valid image files).
        Concatenates the image path, directory separator and image file together.
        Returns the concatenated string.
        :return: String
        """
        image_path = "{}{}{}".format(self.image_path, fa.FileAccess().dir_separator(),
                                     self.image_list[rr(0, len(self.image_list), 1)])
        return image_path

    def display_timer(self):
        """
        Displays a timer with the number of Days, Hours, Minutes and Seconds till Christmas on a
        random image background.
        If it is Christmas displays christmas saying it is Christmas.
        :return:
        """
        image_path = self.random_image
        self.image = cv2.imread(image_path)
        cv2.namedWindow("MyImage", cv2.WND_PROP_FULLSCREEN)
        cv2.setWindowProperty("MyImage", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

        if self.christmas_day():
            self.image_text("CHRISTMAS COUNTDOWN", (50, 100), 2.4, (0, 0, 255), 7)
            self.image_text(self.text_christmas(), (80, 340), 2.0, (0, 0, 0), 7)
            cv2.imshow("MyImage", self.image)
            cv2.waitKey(2000)
        else:

            for i in range(50):
                """
                Loop for 50 times, at the end of each loop wait 200 millisecond. Calculate the amount of time in Days, Hours, Minutes and Seconds
                till Christmas. Displays a countdown to Christmas.
                """
                self.image = cv2.imread(image_path)
                cv2.namedWindow("MyImage", cv2.WND_PROP_FULLSCREEN)
                cv2.setWindowProperty("MyImage", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
                self.image_text("CHRISTMAS COUNTDOWN", (50, 100), 2.4, (0, 0, 255), 7)
                self.image_text("  D   H  M   S  ", (90, 240), 3.0, (0, 0, 0), 7)
                differance = (self.next_christmas - dt.datetime.now())
                days = int(int(differance.total_seconds()) / 86400)
                hours = int((differance.total_seconds() - days * 86400) / 3600)
                mins = int((differance.total_seconds() - ((days * 86400) + (hours * 3600))) / 60)
                seconds = int((differance.total_seconds() - ((days * 86400) + (hours * 3600) + (mins * 60))))
                countdown = "{:>3}: {:>2}: {:>2}: {:>2}:".format(days, hours, mins, seconds)
                self.image_text(countdown, (90, 350), 3.0, (0, 0, 0), 7)
                cv2.imshow("MyImage", self.image)
                cv2.waitKey(200)

    def text_christmas(self):
        """
        Randomly selects a string item from the self.christmas_text list
        (List of text expression that it is Christmas day) and returns String of
        selected item.
        :return: String
        """
        xmas_text = self.christmas_text[rr(0, len(self.christmas_text), 1)]
        return xmas_text

    def christmas_day(self):
        """
        Returns Ture, if the Month is December and the day is the 25th. False if not.
        :return: Bool
        """
        if self.current_month == 10 and self.current_day == 29:
            return True
        else:
            return False

    def image_text(self, text, position, font_size, colour, font_thickness):
        """
        Takes the parameters for displaying text on a background.
        :param text: String:
        :param position: Tuple:
        :param font_size: Float:
        :param colour: Tuple:
        :param font_thickness: Float:
        :return:
        """
        cv2.putText(
            self.image,
            text=text,
            org=position,
            fontFace=self.image_font,
            fontScale=font_size,
            color=colour,
            thickness=font_thickness
        )

