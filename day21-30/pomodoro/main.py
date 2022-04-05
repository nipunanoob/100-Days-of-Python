from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 15
CHECK_SYMBOL = "✓"
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    window.after_cancel(timer)
    timer_label['text'] = 'Timer'
    canvas.itemconfig(timer_text, text="00:00")
    reps = 0
    check.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 2 != 0:
        timer_label.config(text="Work", fg=GREEN)
        count_down(work_sec)
    elif reps % 2 == 0:
        new_text = check["text"] + CHECK_SYMBOL
        check.config(text=new_text)
        if reps % 8 != 0:
            timer_label.config(text="Break", fg=PINK)
            count_down(short_break_sec)
        else:
            timer_label.config(text="Break", fg=RED)
            count_down(long_break_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    minutes = count // 60
    seconds = count % 60
    canvas.itemconfig(timer_text, text="%02d:%02d" % (minutes, seconds))
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro timer")
window.config(padx=25, pady=5, bg=YELLOW)

timer_label = Label(text='Timer', font=(FONT_NAME, 40, 'bold'), fg=GREEN, bg=YELLOW)
timer_label.grid(row=0, column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill='white', font=(FONT_NAME, 30, 'bold'))
canvas.grid(row=1, column=1)

start_button = Button(text='Start', bg=PINK, highlightthickness=0, bd=0, font=(FONT_NAME, 15, 'bold'),
                      command=start_timer)
start_button.config(padx=20, pady=10)
start_button.grid(row=2, column=0)

reset_button = Button(text='Reset', bg=PINK, highlightthickness=0, bd=0, font=(FONT_NAME, 15, 'bold'),
                      command=reset_timer)
reset_button.config(padx=20, pady=10)
reset_button.grid(row=2, column=3)

check = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 15, 'bold'))
check.grid(row=3, column=1)

window.mainloop()
