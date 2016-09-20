import datetime
import vlc
import time
from tkinter import *


class View():
    def __init__(self, controller):
        self.controller = controller
        self.window = Tk()
        self.window.title("Alarm")

        self.time = Label(self.window)
        self.time.place(relheight=1/4, relwidth=1/2, relx=1/4, rely=1/8)
        self.time.config(bg="gray", text="00 : 00")

        self.confirm = Button(self.window)
        self.confirm.place(relheight=1/4, relwidth=1/2, relx=1/4, rely=5/8)
        self.confirm.config(text="Set Alarm")
        self.confirm["command"] = lambda:self.controller.startAlarm()

        self.plush = Button(self.window)
        self.plush.place(relheight=1/8, relwidth=1/8, relx=1/16, rely=1/8)
        self.plush.config(text="+")
        self.plush["command"] = lambda:self.controller.incHours()

        self.minush = Button(self.window)
        self.minush.place(relheight=1/8, relwidth=1/8, relx=1/16, rely=2/8)
        self.minush.config(text="-")
        self.minush["command"] = lambda:self.controller.decHours()

        self.plusmin = Button(self.window)
        self.plusmin.place(relheight=1/8, relwidth=1/8, relx=13/16, rely=1/8)
        self.plusmin.config(text="+")
        self.plusmin["command"] = lambda:self.controller.incMinutes()

        self.minusmin = Button(self.window)
        self.minusmin.place(relheight=1/8, relwidth=1/8, relx=13/16, rely=2/8)
        self.minusmin.config(text="-")
        self.minusmin["command"] = lambda:self.controller.decMinutes()

    def redraw(self, hours, minutes):
        time = str(hours) + " : " + str(minutes)
        self.time["text"] = time


class Controller():
    def __init__(self, alarm):
        self.minutes = 0
        self.hours = 0
        self.view = View(self)
        self.alarm = alarm

    def incHours(self):
        hours = int(self.hours)
        if hours < 23:
            hours += 1
        else:
            hours = 0
        hours = str(hours)
        if len(hours) == 1:
            hours = "0" + hours
        self.hours = hours
        self.minutes = str(self.minutes)
        if len(self.minutes) == 1:
            self.minutes += "0"

        self.view.redraw(str(self.hours), str(self.minutes))

    def incMinutes(self):
        mins = int(self.minutes)
        if mins < 59:
            mins += 1
        else:
            mins = 0
        mins = str(mins)
        if len(mins) == 1:
            mins = "0" + mins
        self.minutes = mins
        self.hours = str(self.hours)
        if len(self.hours) == 1:
            self.hours += "0"
        self.view.redraw(self.hours, self.minutes)


    def decHours(self):
        hours = int(self.hours)
        if hours > 0:
            hours -= 1
        else:
            hours = 23
        hours = str(hours)
        if len(hours) == 1:
            hours = "0" + hours
        self.hours = hours
        self.minutes = str(self.minutes)
        if len(self.minutes) == 1:
            self.minutes += "0"
        self.view.redraw(self.hours, self.minutes)

    def decMinutes(self):
        mins = int(self.minutes)
        if mins > 0:
            mins -= 1
        else:
            mins = 59
        mins = str(mins)
        if len(mins) == 1:
            mins = "0" + mins
        self.minutes = mins
        self.hours = str(self.hours)
        if len(self.hours) == 1:
            self.hours += "0"
        self.view.redraw(self.hours, self.minutes)

    def startAlarm(self):
        self.alarm.wakeUp(int(self.hours), int(self.minutes))

    def start(self):
        self.view.window.mainloop()

class Alarm():
    def __init__(self, sound):
        self.sound = sound

    def wakeUp(self, hour, minute):
        wantedtime = datetime.time(hour,minute).strftime("%H:%M")
        currenttime = datetime.datetime.now().time().strftime("%H:%M")

        while True:
            currenttime = datetime.datetime.now().time().strftime("%H:%M")
            if wantedtime==currenttime:
                self.sound.play()
                time.sleep(60)
                break


p = vlc.MediaPlayer('/Users/dennisledwon/Music/Freestyle.mp3')
alarm = Alarm(p)

control = Controller(alarm)
control.start()
