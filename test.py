import os
import time as ti

viedoFile = []
cwd = os.getcwd()
print(cwd)

folder = "video"


full = cwd + "\\" + folder
full2 = cwd + "/" + folder
print(full)
for file in os.listdir(full):
    if file.endswith(".mp4"):
        viedoFile.append(file)
print(viedoFile)
print(full2)
for file in os.listdir(full2):
    if file.endswith(".mp4"):
        viedoFile.append(file)

gpio = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]

def all_on():
    print("all gpio on")

def all_off():
    print("all gpio off")

def select_day(day):
    print("turn on all selected days.")

if int(ti.strftime('%m')) == 9:
    print(ti.strftime('%d'))
    day = int(ti.strftime('%d'))
    if day > 24 or int(ti.strftime('%m')) == 1:
        all_on()
    else:
        for i in range(day):
            print("{}".format(gpio[i]))
else:
    all_off()

print(ti.strftime('%H'))

x = int(ti.strftime('%H'))
y = (float(ti.strftime('%M')) / 100)
print(x)
print(y)
z = float(x + y)
print(z)

k = 4
t1 = 753
t2 = 1107
ct = int(ti.strftime('%H') + ti.strftime('%M'))
print("ct = {}".format(ct))

def days_on():
    if t1 < int(ti.strftime('%H%M')) < t2:
        print("In time range")
    else:
        print("Too late or early")

days_on()
print(int(ti.strftime('%H%M')) / 100)
