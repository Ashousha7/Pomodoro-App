from cProfile import label
from cgitb import reset
from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1500
SHORT_BREAK_MIN = 6000
LONG_BREAK_MIN = 9000
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #

def reset_time():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text,text="00:00")
    timer_label.config(text="Timer",fg=GREEN)
    check_label.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():

    global reps
    reps+=1

    work_sec = WORK_MIN
    short_break_sec = SHORT_BREAK_MIN
    long_break_sec = LONG_BREAK_MIN

    if reps %8==0:
        timer_label.config(text="Break", fg=RED)
        count_down(long_break_sec)

    elif reps %2 ==0:
        timer_label.config(text="Break", fg=PINK)
        count_down(short_break_sec)
    else:
        timer_label.config(text="Work",fg=GREEN)
        count_down(work_sec)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):

    count_min = math.floor(count/60)
    count_sec = count%60

    if count_sec <10:
        count_sec=f"0{count_sec}"

    canvas.itemconfig(timer_text,text = f"{count_min}:{count_sec}")
    if count>0:
       global timer
       timer = window.after(1000, count_down,count-1)
    else:
        start_timer()
        mark = ""
        for _ in range(math.floor(reps/2)):
            mark = mark +"✔"

        check_label.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #

window =Tk()

window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)

# def say(thing,a,b):
#     print(thing)
#     print(a)
#     print(b)
#
# window.after(1000,say,"Hello","a","b")



#Label 1
timer_label = Label(text="Timer",fg=GREEN,font=(FONT_NAME,50),bg=YELLOW)
timer_label.grid(row = 0,column = 1)

#Label 2
check_label = Label(text ="",fg=GREEN,font=(FONT_NAME,8,"bold"),bg=YELLOW)
check_label.grid(row = 3 , column = 1)

#Start Button
start_button = Button(text = "Start",fg="black",bg="white",font=(FONT_NAME,8,"bold"),command=start_timer)
start_button.grid(row=2,column=0)

#Reset Button
start_button = Button(text = "Reset",fg="black",bg="white",font=(FONT_NAME,8,"bold"),command=reset_time)
start_button.grid(row=2,column=2)

canvas = Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)


tomato_pic = PhotoImage(file = "tomato.png")
canvas.create_image(100,112,image =tomato_pic)
timer_text = canvas.create_text(100,130,text="00:00",fill="white",font =(FONT_NAME,35,"bold"))

canvas.grid(row = 1 , column = 1)



window.mainloop()