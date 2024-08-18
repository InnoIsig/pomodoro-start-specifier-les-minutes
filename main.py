from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#06D001"
YELLOW = "#021526"
WITH = "#FFFFFF"
FONT_NAME = "Courier"
WORK_MIN = 45
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# TODO 9 : ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(time_text, text="00:00")
    title_label.config(text="L'heure")
    check_marks.config(text="")
    global reps
    reps = 0
# TODO 6 : ---------------------------- TIMER MECHANISM redemarage des minutes ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
# TODO 7 : Conditions de nombres de sences de travail
    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Grande Pause", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="Petite Pause", fg=PINK)
    else:
        count_down(work_sec)
        title_label.config(text="Travail", fg=GREEN)

# TODO 5 ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(time_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        #TODO 8 ajoutons la marque pour prouver la validation de seance de travail
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
        check_marks.config(text=marks)



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro Project")
window.config(padx=100, pady=50, bg=YELLOW)



# TODO 2 : Interface utilisateur pour manupuler le temps
title_label = Label(text="L'heure", bg=YELLOW, fg=WITH, font=(FONT_NAME, 40, "bold"))
title_label.grid(column=1, row=0)


# TODO 1 : Création de l'image et ajustage et interface utilisateur
canvas = Canvas(width=200, height=223, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
time_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


# TODO 3 : Boutton pour demarrer le travail
start_button1 = Button(text="Commencer", highlightthickness=0, command=start_timer)
start_button1.grid(column=0, row=2)
start_button2 = Button(text="Réinitialiser", highlightthickness=0, command=reset_timer)
start_button2.grid(column=2, row=2)

# TODO 4 : check marks code
check_marks = Label(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 18, "bold"))
check_marks.grid(column=1, row=3)








window.mainloop()
