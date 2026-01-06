from tkinter import *
from time import strftime
import winsound

top = Tk()
top.title("Digital Clock")
top.geometry("700x400")   # 👈 half / normal screen
top.configure(bg="black")

alarm_time = StringVar()
last_hour = ""

# Time function
def time():
    global last_hour
    current_time = strftime('%I : %M : %S %p')
    current_date = strftime('%A, %d %B %Y')
    current_hour = strftime('%H')

    time_lbl.config(text=current_time)
    date_lbl.config(text=current_date)

    # 🔔 Hour change sound
    if current_hour != last_hour:
        winsound.Beep(800, 400)
        last_hour = current_hour

    # ⏰ Alarm check
    if alarm_time.get() == strftime('%I:%M %p'):
        winsound.Beep(1000, 1500)

    time_lbl.after(1000, time)

# Change colors
def set_color(bg, fg):
    top.configure(bg=bg)
    time_lbl.configure(bg=bg, fg=fg)
    date_lbl.configure(bg=bg)
    btn_frame.configure(bg=bg)
    alarm_frame.configure(bg=bg)

# Time label
time_lbl = Label(
    top,
    font=('digital-7', 60, 'bold'),
    bg='black',
    fg='red'
)
time_lbl.pack(pady=15)

# Date label
date_lbl = Label(
    top,
    font=('Arial', 18),
    bg='black',
    fg='white'
)
date_lbl.pack()

# Color buttons
btn_frame = Frame(top, bg="black")
btn_frame.pack(pady=15)

Button(btn_frame, text="Red",
       command=lambda: set_color("black", "red")).grid(row=0, column=0, padx=10)
Button(btn_frame, text="Green",
       command=lambda: set_color("black", "lime")).grid(row=0, column=1, padx=10)
Button(btn_frame, text="Blue",
       command=lambda: set_color("black", "cyan")).grid(row=0, column=2, padx=10)
Button(btn_frame, text="White",
       command=lambda: set_color("black", "white")).grid(row=0, column=3, padx=10)

# Alarm section
alarm_frame = Frame(top, bg="black")
alarm_frame.pack(pady=15)

Label(
    alarm_frame,
    text="Set Alarm (HH:MM AM/PM)",
    fg="white",
    bg="black",
    font=('Arial', 14)
).grid(row=0, column=0, padx=10)

Entry(
    alarm_frame,
    textvariable=alarm_time,
    font=('Arial', 14),
    width=10
).grid(row=0, column=1)

time()
top.mainloop()
