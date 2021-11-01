import cv2
import os
import random
import time as ti
import display_trivia as tr
import display_video as vi
import timer as cd
import jokes as jo


def main():
    trivia = tr.DisplayTrivia().display_trivia()
    timer = cd.Timer().display_timer()
    joke = jo.Jokes().tell_joke()
    video = vi.DisplayVideo()

    content = [trivia, timer, joke, video]

    for i in content:
        i

main()


