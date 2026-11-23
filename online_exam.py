from tkinter import *

BG_MAIN = "#0F172A"
BG_CARD = "#1E293B"
FG_TEXT = "#F8FAFC"
FG_ACCENT = "#38BDF8"
BTN_BG = "#4F46E5"
BTN_FG = "#FFFFFF"
BTN_ACTIVE = "#4338CA"

su = Tk()
su.title("Online Examination System")
su.geometry("600x500")
su.config(bg=BG_MAIN, padx=20, pady=15)

questions = [
    "1. Which language is used for Python programming?",
    "2. Which keyword is used to define a function?",
    "3. Which function displays output?",
    "4. Which symbol is used for comments?",
    "5. Which data type stores True or False?"
]

options = [
    ["Python", "Java", "C++", "HTML"],
    ["function", "def", "define", "fun"],
    ["input()", "print()", "show()", "display()"],
    ["//", "#", "/*", "<!--"],
    ["int", "str", "bool", "float"]
]

answers = ["Python", "def", "print()", "#", "bool"]

i = 0
score = 0

L1 = Label(
    su, text="Student Name",
    font=("arial", 15, "bold"),
    bg=BG_MAIN, fg=FG_ACCENT
)
L1.grid(row=0, column=0, pady=10, sticky="w", padx=(0, 10))

E1 = Entry(
    su, font=("arial", 15),
    bg=BG_CARD, fg=FG_TEXT,
    insertbackground=FG_TEXT
)
E1.grid(row=0, column=1, pady=10, sticky="w")

Q1 = Label(
    su, text="",
    font=("arial", 15, "bold"),
    bg=BG_MAIN, fg=FG_TEXT,
    wraplength=540, justify="left"
)
Q1.grid(row=1, column=0, columnspan=2, pady=20, sticky="w")

v = StringVar()

radio_style = {
    "variable": v,
    "value": "",
    "font": ("arial", 14),
    "bg": BG_MAIN,
    "fg": FG_TEXT,
    "activebackground": BG_MAIN,
    "activeforeground": FG_ACCENT,
    "selectcolor": BG_CARD
}

R1 = Radiobutton(su, text="", **radio_style)
R1.grid(row=2, column=0, columnspan=2, sticky="w", pady=3)

R2 = Radiobutton(su, text="", **radio_style)
R2.grid(row=3, column=0, columnspan=2, sticky="w", pady=3)

R3 = Radiobutton(su, text="", **radio_style)
R3.grid(row=4, column=0, columnspan=2, sticky="w", pady=3)

R4 = Radiobutton(su, text="", **radio_style)
R4.grid(row=5, column=0, columnspan=2, sticky="w", pady=3)


def show_question():
    Q1.config(text=questions[i])

    R1.config(text=options[i][0], value=options[i][0])
    R2.config(text=options[i][1], value=options[i][1])
    R3.config(text=options[i][2], value=options[i][2])
    R4.config(text=options[i][3], value=options[i][3])

    v.set("")


def next_question():
    global i, score

    if v.get() == "":
        return

    if v.get() == answers[i]:
        score = score + 1

    i = i + 1

    if i < 5:
        show_question()
    else:
        Q1.config(text="Examination Completed!", fg=FG_ACCENT)

        R1.config(text="")
        R2.config(text="")
        R3.config(text="")
        R4.config(text="")

        B1.config(state=DISABLED)

        student = E1.get().strip() or "Anonymous"
        L2.config(
            text=f"Student: {student}\nYour Score: {score}/5"
        )


B1 = Button(
    su, text="Next Question",
    font=("arial", 14, "bold"),
    bg=BTN_BG, fg=BTN_FG,
    activebackground=BTN_ACTIVE, activeforeground=BTN_FG,
    command=next_question
)
B1.grid(row=6, column=0, columnspan=2, pady=20, sticky="w")


L2 = Label(
    su, text="",
    font=("arial", 15, "bold"),
    bg=BG_MAIN, fg="#4ADE80",
    justify="left"
)
L2.grid(row=7, column=0, columnspan=2, sticky="w")


show_question()


while True:
    try:
        su.update()
    except TclError:
        break
s
