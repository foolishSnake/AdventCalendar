import os
import time as ti

viedoFile = []
cwd = os.getcwd()

folder = "video"
# on_time = 1730
# off_time = 1030

on_time = 829
off_time = 831
led_on = False


# full = cwd + "\\" + folder
# full2 = cwd + "/" + folder
# print(full)
# for file in os.listdir(full):
#     if file.endswith(".mp4"):
#         viedoFile.append(file)
# print(viedoFile)
# print(full2)
# for file in os.listdir(full2):
#     if file.endswith(".mp4"):
#         viedoFile.append(file)

gpio = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]

def all_on():
    print("all gpio on")
    led_on = True

def all_off():
    print("all gpio off")
    led_on = False

# def select_day(day):
#     print("turn on all selected days.")
#
#     if int(ti.strftime('%m')) == 9:
#         print(ti.strftime('%d'))
#         day = int(ti.strftime('%d'))
#         if day > 24 or int(ti.strftime('%m')) == 1:
#             all_on()
#         else:
#             for i in range(day):
#                 print("{}".format(gpio[i]))
#     else:
#         all_off()


def days_on():
    """
    If month is November does not turn on any leds. If month is December and date is lower than 24th, turn
    on leds upto the current date. If date is the 24th ot later turns on all leds.
    :return:
    """
    month = int(ti.strftime('%m'))
    day = int(ti.strftime('%d'))

    if month > 1:
        all_off()
        return False
    elif month == 12 and day < 24:
        days_on(days)
        return False
    else:
        all_on()
        return False


def play_video():
    """
    Randomlys selects a video to play.
    :return:
    """

    pass

def countdown_timer():
    """
    Will display the amount of days, hours and minutes untill Christmas.
    :return:
    """
    pass

def joke():
    """
    Displays a randon joke.
    :return:
    """

    pass

def trivea():
    """
    Displays a random bit christmas travea.
    :return:
    """

    pass

def advent_on():
    """
    Turns the calander on and off based on the time
    :return:
    """
    current_time = int(ti.strftime('%H%M'))

    if on_time <= int(ti.strftime('%H%M')) < off_time:
        return True
    else:
        return False

def screen_off()
    """
    Turns the screen on and off.
    :return: 
    """

    pass


switch = True

# while switch:
#     if advent_on():
#         print("I am on!")
#     else:
#         print("I am off!")
#         switch = False
#     ti.sleep(10)

print(int(ti.strftime('%H%M')))
if on_time <= int(ti.strftime('%H%M')) < off_time:
    print(True)
else:
    print(False)

