import os
import sys
import csv


class FileAccess:
    def __init__(self):
        self.image_type = [".jpg", ".jpeg", ".png"]
        self.video_type: list[str] = [".mp4"]

    @property
    def video_path(self):
        return "{}{}{}{}".format(os.getcwd(), self.dir_separator(), "video", self.dir_separator())

    @property
    def images_path(self):
        return "{}{}{}{}".format(os.getcwd(), self.dir_separator(), "images", self.dir_separator())

    @property
    def joke_path(self):
        return "{}{}{}{}{}".format(os.getcwd(), self.dir_separator(), "joke", self.dir_separator(),
                                   "jokes.csv")
    @property
    def joke_image_path(self):
        return "{}{}{}{}{}".format(os.getcwd(), self.dir_separator(), "joke", self.dir_separator(),
                                   "images")

    @property
    def trivia_path(self):
        return "{}{}{}{}{}".format(os.getcwd(), self.dir_separator(), "trivia", self.dir_separator(),
                                   "trivia.csv")

    @staticmethod
    def dir_separator():
        if sys.platform == "win32":
            return "\\"
        else:
            return "/"

    def get_images_files(self):
        return self.media_files(self.images_path, self.image_type)

    def get_video_files(self):
        return self.media_files(self.video_path, self.video_type)

    def get_trivia(self):
        return self.read_text(self.trivia_path)

    def get_joke(self):
        return self.read_text(self.joke_path)

    @staticmethod
    def media_files(path, file_type):
        files = []

        try:
            for file in os.listdir(path):
                for j in file_type:
                    if file.endswith(j):
                        files.append(file)
        except FileNotFoundError:
            return None

        return files

    @staticmethod
    def read_text(file_name):

        try:
            with open(file_name, 'r', encoding="utf8") as f:
                reader = csv.reader(f)
                text_list = list(reader)
            return text_list
        except FileNotFoundError:
            return None
