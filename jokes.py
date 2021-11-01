import cv2
import file_access as fa
import display_trivia as dt
from random import randrange as rr


class Jokes:

    def __init__(self):
        self.joke_questions = fa.FileAccess().get_joke()
        self.response = ["I dont know!", "Oh just tell me!", "I hope this is not another cheesy joke!",
                         "let us just get this over with!"]
        self.reaction = ["Good Grief", "That is like so UNFUNNY", "Where do you get these from", "Oh HA HA",
                         "That was the best one so far", "I know how Statler and Waldorf felt",
                         "WHAT", "Bro not even a joke", "That was so sad it brought a tear to my eye",
                         "Dont give up the day job"]
        self.joke_path = fa.FileAccess().joke_image_path
        self.dir_separator = fa.FileAccess().dir_separator()
        self.tell_path = "{}{}{}".format(self.joke_path, self.dir_separator, "tell.png")
        self.response_path = "{}{}{}".format(self.joke_path, self.dir_separator, "response.png")
        self.answer_path = "{}{}{}".format(self.joke_path, self.dir_separator, "answer.png")
        self.reaction_path = "{}{}{}".format(self.joke_path, self.dir_separator, "reaction.png")
        self.image = None
        self.image_font = cv2.cv2.FONT_HERSHEY_DUPLEX
        self.current_joke = None
        self.display_trivia = dt.DisplayTrivia()

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

    def tell_joke(self):
        x_space = 280
        y_space = 180
        line_space = 60
        line_length = 18
        self.image = cv2.imread(self.tell_path)
        self.current_joke = self.display_trivia.text_convert(self.random_joke, line_length)
        for i in self.current_joke[0]:
            self.image_text(i, (x_space, y_space ), 2.0, (0, 0, 0), 4)
            y_space += line_space

        cv2.namedWindow("MyImage", cv2.WND_PROP_FULLSCREEN)
        cv2.setWindowProperty("MyImage", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        cv2.imshow("MyImage", self.image)
        cv2.waitKey(5000)

        self.response_joke()

    def response_joke(self):
        x_space = 30
        y_space = 180
        line_space = 71
        line_length = 18
        response = self.display_trivia.text_formatted(self.random_response.split(), line_length)
        self.image = cv2.imread(self.response_path)
        for i in response:
            self.image_text(i, (x_space, y_space), 2.4, (0, 0, 0), 4)
            y_space += line_space

        cv2.namedWindow("MyImage", cv2.WND_PROP_FULLSCREEN)
        cv2.setWindowProperty("MyImage", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        cv2.imshow("MyImage", self.image)
        cv2.waitKey(5000)
        self.punchline_joke()

    def punchline_joke(self):
        x_space = 80
        y_space = 180
        line_space = 60
        line_length = 24
        self.image = cv2.imread(self.answer_path)
        for i in self.current_joke[1]:
            self.image_text(i, (x_space, y_space), 2.3, (0, 0, 0), 4)
            y_space += line_space

        cv2.namedWindow("MyImage", cv2.WND_PROP_FULLSCREEN)
        cv2.setWindowProperty("MyImage", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        cv2.imshow("MyImage", self.image)
        cv2.waitKey(5000)
        self.reaction_joke()

    def reaction_joke(self):
        x_space = 520
        y_space = 50
        line_space = 50
        line_length = 18
        self.image = cv2.imread(self.reaction_path)
        reaction = self.display_trivia.text_formatted(self.random_reaction.split(), line_length)
        self.image = cv2.imread(self.reaction_path)
        for i in reaction:
            self.image_text(i, (x_space, y_space), 1.6, (0, 0, 0), 4)
            y_space += line_space

        cv2.namedWindow("MyImage", cv2.WND_PROP_FULLSCREEN)
        cv2.setWindowProperty("MyImage", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        cv2.imshow("MyImage", self.image)
        cv2.waitKey(5000)

    @property
    def random_joke(self):
        return self.joke_questions[rr(0, len(self.joke_questions), 1)]

    @property
    def random_response(self):
        return self.response[rr(0, len(self.response), 1)]

    @property
    def random_reaction(self):
        return self.reaction[rr(0, len(self.reaction), 1)]
