import pyautogui
import datetime
import random
import time
import winsound
import sys

x,y= pyautogui.size()

def window(finish):
    # import datetime
    # now = datetime.datetime.now()
    # today8am = now.replace(hour=8, minute=0, second=0, microsecond=0)
    # now < today8am

    done = finish.replace(second=0, microsecond=0)
    while datetime.datetime.now() < done:
        """ MOVE
        x_move = random.randrange(1,x)
        y_move = random.randrange(1,y)
        pyautogui.moveTo(x_move, y_move, duration = 0.5)
        """
        pyautogui.click(x=1536, y=0)
        time.sleep(10)

def timed():
    if len(sys.argv) == 1:
        correct = True
        while correct:
            mins = input("How many minutes will you be gone?\n")
            answer = input("Is this correct?(y/n)")
            if answer == 'y':
                correct = False
    else:
        mins = sys.argv[1]
    end = datetime.timedelta(minutes=int(mins))
    fine = datetime.datetime.now() + end
    window(fine)
    for x in range(5):
        winsound.Beep(1000, 100)
        time.sleep(1)


if __name__ == "__main__":
    timed()
