from tkinter import *
import time
import math

class window():
    #"s" is the shorthand for "self"
    def __init__(s):
        s.root = Tk()
        s.root.title("Clock")
        s.root.grid()

        s.canvas = Canvas(height = 900, width = 900, bg = "Black")
        s.canvas.grid()

        s.body = s.canvas.create_oval(0, 0, 900, 900, fill = "White")
        s.center = s.canvas.create_oval(400, 400, 500, 500, fill = "Red")

        s.hand = ["","",""]
        for i in range(3):
            s.hand[i] = s.canvas.create_line(450, 450, 450, 0, width = 10)

        timelist = time.asctime().split()
        clocktime = list(timelist[3])

        s.hours = int(str(clocktime[0]) + str(clocktime[1]))
        s.minutes = int(str(clocktime[3]) + str(clocktime[4]))
        s.seconds = int(str(clocktime[6]) + str(clocktime[7]))

        window.counter(s)
        s.root.mainloop()


    def counter(s): #right now we are only focusing on seconds
        if s.seconds == 60:
            s.seconds = 0
            s.minutes += 1

        if s.minutes == 60:
            s.minutes = 0
            s.hours += 1

        if s.hours == 12:
            s.hours = 0

        timelist = [s.seconds, s.minutes, s.hours]
        xcoord = ["","",""]
        ycoord = ["","",""]
        
        for i in range(3): #runs once for each hand
            angle = 6 * timelist[i]
            if i == 2:
                angle = angle * 5
                
            sin = math.sin(math.radians(angle))
            cos = math.cos(math.radians(angle))

            #the following are in respect to the center (400 is length of hand)
            xcoord[i] = int(sin * 400) + 450
            ycoord[i] = 450 - int(cos * 400)

            s.canvas.delete(s.hand[i])
            s.hand[i] = s.canvas.create_line(450, 450, xcoord[i], ycoord[i], width = 10)


        s.seconds += 1
        s.canvas.delete(s.center)
        s.center = s.canvas.create_oval(400, 400, 500, 500, fill = "Red")
        s.root.after(1000, window.counter, s)

        



if __name__ == "__main__":
    clock = window()
    quit()
