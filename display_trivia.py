import cv2
import imutils as im
import file_access as fa
import random


class DisplayTrivia:

    def __init__(self):
        self.trivia_questions = fa.FileAccess().get_trivia()
        self.background_images = fa.FileAccess().get_images_files()
        self.scroll_limit = 35
        self.image_path = fa.FileAccess().images_path
        self.trivia_font = cv2.FONT_HERSHEY_DUPLEX
        self.heading_font = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
        self.image = None

    def text_convert(self, text, scroll_limit):
        """
        Takes a list with two list of text. Index 1 is the Question, Index 2 the answer.
        Splits each list on a space into a list of each word in the text.
        Text is passed to the text_formatted method.
        :param text: List of 2 List each list is a String
        :param scroll_limit: Integer of the max number of characters in each line.
        :return: List with 2 formatted list of text lines.
        """
        question = text[0].split()
        answer = text[1].split()
        question_list = self.text_formatted(question, scroll_limit)
        answer_list = self.text_formatted(answer, scroll_limit)

        return [question_list, answer_list]

    @staticmethod
    def text_formatted(text_list, scroll_limit):
        output_list = []
        out = ""
        for index, i in enumerate(text_list):
            if len(out) + len(i) > scroll_limit:
                output_list.append(out)
                out = "{} ".format(i)

                if index == len(text_list) - 1:
                    output_list.append(out)
            else:
                out += "{} ".format(i)
                if index == len(text_list) - 1:
                    output_list.append(out)

        return output_list

    def random_image(self):
        return self.background_images[random.randrange(len(self.background_images) - 1)]

    def random_question(self):
        return self.trivia_questions[random.randrange(len(self.trivia_questions) - 1)]

    def display_trivia(self):
        question = self.text_convert(self.random_question(), self.scroll_limit)
        display_image_path = "{}{}".format(self.image_path, self.random_image())
        self.image = cv2.imread(display_image_path)
        self.image = im.resize(self.image, width=1024, height=600)
        cv2.namedWindow("MyImage", cv2.WND_PROP_FULLSCREEN)
        cv2.setWindowProperty("MyImage", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        # Using cv2.putText()
        position = (10, 50)
        space_y = 50
        y_axis = 240
        x_axis = 20

        self.image_text("Trivia Time", (300, 90), 3.2, (0, 0, 255), self.heading_font, 7)
        self.image_text("Question:", (x_axis, 180), 2.0, (255, 0, 0), self.trivia_font, 7)

        for i in question[0]:
            self.image_text(i, (x_axis, y_axis), 1.5, (0, 0, 0), self.trivia_font, 3)
            y_axis += space_y
        cv2.imshow("MyImage", self.image)
        cv2.waitKey(6000)
        y_axis += 25

        self.image_text("Answer", (x_axis, y_axis), 2.0, (0, 0, 255), self.trivia_font, 3)
        y_axis += 60

        for j in question[1]:
            self.image_text(j, (x_axis, y_axis), 1.5, (0, 0, 0), self.trivia_font, 3)
            y_axis += space_y

        cv2.imshow("MyImage", self.image)
        cv2.waitKey(5000)

    def image_text(self, text, position, font_size, colour, font, font_thickness):
        """
        Takes the parameters for displaying text on a background.
        :param text: String:
        :param position: Tuple:
        :param font_size: Float:
        :param colour: Tuple:
        :param font: Font object
        :param font_thickness: Float:
        :return:
        """
        cv2.putText(
            self.image,
            text=text,
            org=position,
            fontFace=font,
            fontScale=font_size,
            color=colour,
            thickness=font_thickness
        )
