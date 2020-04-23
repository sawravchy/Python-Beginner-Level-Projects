import tkinter
from tkinter import *
from tkinter import messagebox

root_window = tkinter.Tk()
root_window.title("Calculator")
root_window.geometry("350x550")
root_window.configure(background="#1D2426")
root_window.resizable(0, 0)

# Functions
# Functions for Button Hover Effect


def enter1(event):
    btn1.config(bg="#545859", fg="#DDDDDD")


def left1(event):
    btn1.config(
        bg="#1D2426",
        fg="#EA185F",
    )


def enter2(event):
    btn2.config(bg="#545859", fg="#DDDDDD")


def left2(event):
    btn2.config(
        bg="#1D2426",
        fg="#DDDDDD",
    )


def enter3(event):
    btn3.config(bg="#545859", fg="#DDDDDD")


def left3(event):
    btn3.config(
        bg="#1D2426",
        fg="#DDDDDD",
    )


def enter4(event):
    btn4.config(bg="#F8585C", fg="#DDDDDD")


def left4(event):
    btn4.config(
        bg="#F04F54",
        fg="#FAFAFA",
    )


def enter5(event):
    btn5.config(bg="#545859", fg="#DDDDDD")


def left5(event):
    btn5.config(
        bg="#1D2426",
        fg="#DDDDDD",
    )


def enter6(event):
    btn6.config(bg="#545859", fg="#DDDDDD")


def left6(event):
    btn6.config(
        bg="#1D2426",
        fg="#DDDDDD",
    )


def enter7(event):
    btn7.config(bg="#545859", fg="#DDDDDD")


def left7(event):
    btn7.config(
        bg="#1D2426",
        fg="#DDDDDD",
    )


def enter8(event):
    btn8.config(bg="#F8585C", fg="#DDDDDD")


def left8(event):
    btn8.config(
        bg="#F04F54",
        fg="#FAFAFA",
    )


def enter9(event):
    btn9.config(bg="#545859", fg="#DDDDDD")


def left9(event):
    btn9.config(
        bg="#1D2426",
        fg="#DDDDDD",
    )


def enter10(event):
    btn10.config(bg="#545859", fg="#DDDDDD")


def left10(event):
    btn10.config(
        bg="#1D2426",
        fg="#DDDDDD",
    )


def enter11(event):
    btn11.config(bg="#545859", fg="#DDDDDD")


def left11(event):
    btn11.config(
        bg="#1D2426",
        fg="#DDDDDD",
    )


def enter12(event):
    btn12.config(bg="#F8585C", fg="#DDDDDD")


def left12(event):
    btn12.config(
        bg="#F04F54",
        fg="#DDDDDD",
    )


def enter13(event):
    btn13.config(bg="#545859", fg="#DDDDDD")


def left13(event):
    btn13.config(
        bg="#1D2426",
        fg="#DDDDDD",
    )


def enter14(event):
    btn14.config(bg="#545859", fg="#DDDDDD")


def left14(event):
    btn14.config(
        bg="#1D2426",
        fg="#DDDDDD",
    )


def enter15(event):
    btn15.config(bg="#545859", fg="#DDDDDD")


def left15(event):
    btn15.config(
        bg="#1D2426",
        fg="#DDDDDD",
    )


def enter16(event):
    btn16.config(bg="#F8585C", fg="#DDDDDD")


def left16(event):
    btn16.config(
        bg="#F04F54",
        fg="#FAFAFA",
    )


def enter17(event):
    btn17.config(bg="#545859", fg="#DDDDDD")


def left17(event):
    btn17.config(
        bg="#1D2426",
        fg="#DDDDDD",
    )


def enter18(event):
    btn18.config(bg="#545859", fg="#DDDDDD")


def left18(event):
    btn18.config(
        bg="#1D2426",
        fg="#DDDDDD",
    )


def enter19(event):
    btn19.config(bg="#545859", fg="#DDDDDD")


def left19(event):
    btn19.config(
        bg="#1D2426",
        fg="#EA185F",
    )


def enter20(event):
    btn20.config(bg="#545859", fg="#F7C754")


def left20(event):
    btn20.config(
        bg="#FEC10E",
        fg="#1E2326",
    )


#Button clicked functions
val = ""
storevalue = 0
operator = ""


def btn1click():
    global storevalue
    global operator
    global val
    storevalue = 0
    operator = ""
    val = ""
    data.set(val)


def btn20click():
    global storevalue
    global operator
    global val
    val1 = val
    if operator == "+":
        x = int((val.split("+")[1]))
        result = storevalue + x
        data.set(result)
        val = str(result)
    elif operator == "-":
        x = int(val.split("-")[1])
        result = storevalue - x
        data.set(result)
        val = str(result)
    elif operator == "*":
        x = int(val.split("*")[1])
        result = storevalue * x
        data.set(result)
        val = str(result)
    elif operator == "/":
        x = int(val.split("÷")[1])
        if x == 0:
            messagebox.showerror("Error", "Divide by 0 is not allowed")
            storevalue = ""
            val = ""
            data.set(val)
        else:
            result = storevalue / x
            data.set(result)
            val = str(result)


def btn4click():
    global storevalue
    global operator
    global val
    storevalue = int(val)
    operator = "/"
    val = val + "÷"
    data.set(val)


def btn8click():
    global storevalue
    global operator
    global val
    storevalue = int(val)
    operator = "*"
    val = val + "*"
    data.set(val)


def btn12click():
    global storevalue
    global operator
    global val
    storevalue = int(val)
    operator = "-"
    val = val + "-"
    data.set(val)


def btn16click():
    global storevalue
    global operator
    global val
    storevalue = int(val)
    operator = "+"
    val = val + "+"
    data.set(val)


def btn5click():
    global val
    val = val + "7"
    data.set(val)


def btn6click():
    global val
    val = val + "8"
    data.set(val)


def btn7click():
    global val
    val = val + "9"
    data.set(val)


def btn9click():
    global val
    val = val + "4"
    data.set(val)


def btn10click():
    global val
    val = val + "5"
    data.set(val)


def btn11click():
    global val
    val = val + "6"
    data.set(val)


def btn13click():
    global val
    val = val + "1"
    data.set(val)


def btn14click():
    global val
    val = val + "2"
    data.set(val)


def btn15click():
    global val
    val = val + "3"
    data.set(val)


def btn17click():
    global val
    val = val + "0"
    data.set(val)


def btn18click():
    print("Not Work")


#///////////////
resultrow = Frame(root_window, bg="#DDDDDD", height=130, bd=1)
resultrow.pack(
    expand=True,
    fill="both",
)
btnrow1 = Frame(root_window, bg="#A8A8A8", bd=0.4)
btnrow1.pack(
    expand=True,
    fill="both",
)
btnrow2 = Frame(root_window, bg="#A8A8A8", bd=0.4)
btnrow2.pack(
    expand=True,
    fill="both",
)
btnrow3 = Frame(root_window, bg="#A8A8A8", bd=0.4)
btnrow3.pack(
    expand=True,
    fill="both",
)
btnrow4 = Frame(root_window, bg="#A8A8A8", bd=0.4)
btnrow4.pack(
    expand=True,
    fill="both",
)
btnrow5 = Frame(root_window, bg="#A8A8A8", bd=0.4)
btnrow5.pack(
    expand=True,
    fill="both",
)
btn1 = Button(btnrow1,
              text="C",
              font=(
                  "Paytone One",
                  18,
              ),
              bg="#1D2426",
              fg="#EA185F",
              bd=0.4,
              command=btn1click)
btn1.pack(side=LEFT, expand=True, fill="both")
btn1.bind("<Enter>", enter1)
btn1.bind("<Leave>", left1)
btn2 = Button(
    btnrow1,
    text="+/-",
    font=("Paytone One", 18),
    bg="#1D2426",
    fg="#DDDDDD",
    bd=0.4,
)
btn2.pack(
    side=LEFT,
    expand=True,
    fill="both",
)
btn2.bind("<Enter>", enter2)
btn2.bind("<Leave>", left2)
btn3 = Button(btnrow1,
              text="%",
              font=("Paytone One", 18),
              bg="#1D2426",
              fg="#DDDDDD",
              bd=0.4)
btn3.pack(
    side=LEFT,
    expand=True,
    fill="both",
)
btn3.bind("<Enter>", enter3)
btn3.bind("<Leave>", left3)
btn4 = Button(btnrow1,
              text="÷",
              font=("Paytone One", 22),
              bg="#F04F54",
              fg="#FAFAFA",
              bd=0.3,
              command=btn4click)
btn4.pack(
    side=LEFT,
    expand=True,
    fill="both",
)
btn4.bind("<Enter>", enter4)
btn4.bind("<Leave>", left4)
btn5 = Button(btnrow2,
              text="7",
              font=("Paytone One", 18),
              bg="#1D2426",
              fg="#DDDDDD",
              bd=0.4,
              command=btn5click)
btn5.pack(
    side=LEFT,
    expand=True,
    fill="both",
)
btn5.bind("<Enter>", enter5)
btn5.bind("<Leave>", left5)
btn6 = Button(btnrow2,
              text="8",
              font=("Paytone One", 20),
              bg="#1D2426",
              fg="#DDDDDD",
              bd=0.4,
              command=btn6click)
btn6.pack(
    side=LEFT,
    expand=True,
    fill="both",
)
btn6.bind("<Enter>", enter6)
btn6.bind("<Leave>", left6)
btn7 = Button(btnrow2,
              text="9",
              font=("Paytone One", 20),
              bg="#1D2426",
              fg="#DDDDDD",
              bd=0.4,
              command=btn7click)
btn7.pack(
    side=LEFT,
    expand=True,
    fill="both",
)
btn7.bind("<Enter>", enter7)
btn7.bind("<Leave>", left7)
btn8 = Button(btnrow2,
              text="x",
              font=("Verdana", 18),
              bg="#F04F54",
              fg="#FAFAFA",
              bd=0.4,
              command=btn8click)
btn8.pack(
    side=LEFT,
    expand=True,
    fill="both",
)
btn8.bind("<Enter>", enter8)
btn8.bind("<Leave>", left8)
btn9 = Button(btnrow3,
              text="4",
              font=("Paytone One", 20),
              bg="#1D2426",
              fg="#DDDDDD",
              bd=0.4,
              command=btn9click)
btn9.pack(
    side=LEFT,
    expand=True,
    fill="both",
)
btn9.bind("<Enter>", enter9)
btn9.bind("<Leave>", left9)
btn10 = Button(btnrow3,
               text="5",
               font=("Paytone One", 20),
               bg="#1D2426",
               fg="#DDDDDD",
               bd=0.4,
               command=btn10click)
btn10.pack(
    side=LEFT,
    expand=True,
    fill="both",
)
btn10.bind("<Enter>", enter10)
btn10.bind("<Leave>", left10)
btn11 = Button(btnrow3,
               text="6",
               font=("Paytone One", 20),
               bg="#1D2426",
               fg="#DDDDDD",
               bd=0.4,
               command=btn11click)
btn11.pack(
    side=LEFT,
    expand=True,
    fill="both",
)
btn11.bind("<Enter>", enter11)
btn11.bind("<Leave>", left11)
btn12 = Button(btnrow3,
               text="-",
               font=("PVerdana", 24),
               bg="#F04F54",
               fg="#DDDDDD",
               bd=0.4,
               command=btn12click)
btn12.pack(
    side=LEFT,
    expand=True,
    fill="both",
)
btn12.bind("<Enter>", enter12)
btn12.bind("<Leave>", left12)

btn13 = Button(btnrow4,
               text="1",
               font=("Paytone One", 20),
               bg="#1D2426",
               fg="#DDDDDD",
               bd=0.4,
               command=btn13click)
btn13.pack(
    side=LEFT,
    expand=True,
    fill="both",
)
btn13.bind("<Enter>", enter13)
btn13.bind("<Leave>", left13)
btn14 = Button(btnrow4,
               text="2",
               font=("Paytone One", 20),
               bg="#1D2426",
               fg="#DDDDDD",
               bd=0.4,
               command=btn14click)
btn14.pack(
    side=LEFT,
    expand=True,
    fill="both",
)
btn14.bind("<Enter>", enter14)
btn14.bind("<Leave>", left14)
btn15 = Button(btnrow4,
               text="3",
               font=("Paytone One", 20),
               bg="#1D2426",
               fg="#DDDDDD",
               bd=0.4,
               command=btn15click)
btn15.pack(
    side=LEFT,
    expand=True,
    fill="both",
)
btn15.bind("<Enter>", enter15)
btn15.bind("<Leave>", left15)
btn16 = Button(btnrow4,
               text="+",
               font=("Paytone One", 19),
               bg="#F04F54",
               fg="#FAFAFA",
               bd=0.4,
               command=btn16click)
btn16.pack(
    side=LEFT,
    expand=True,
    fill="both",
)
btn16.bind("<Enter>", enter16)
btn16.bind("<Leave>", left16)

btn17 = Button(btnrow5,
               text="0",
               font=("Paytone One", 20),
               bg="#1D2426",
               fg="#DDDDDD",
               bd=0.4,
               command=btn17click)
btn17.pack(
    side=LEFT,
    expand=True,
    fill="both",
)
btn17.bind("<Enter>", enter17)
btn17.bind("<Leave>", left17)

btn18 = Button(btnrow5,
               text=".",
               font=("Paytone One", 20),
               bg="#1D2426",
               fg="#DDDDDD",
               bd=0.4,
               command=btn18click)
btn18.pack(
    side=LEFT,
    expand=True,
    fill="both",
)
btn18.bind("<Enter>", enter18)
btn18.bind("<Leave>", left18)
btn19 = Button(btnrow5,
               text="DEL",
               font=("Paytone One", 13),
               bg="#1D2426",
               fg="#ED1B4C",
               bd=0.4)
btn19.pack(
    side=LEFT,
    expand=True,
    fill="both",
)
btn19.bind("<Enter>", enter19)
btn19.bind("<Leave>", left19)
btn20 = Button(btnrow5,
               text="=",
               font=("Verdana", 17),
               bg="#FEC10E",
               fg="#1E2326",
               bd=0.4,
               command=btn20click)
btn20.pack(
    side=LEFT,
    expand=True,
    fill="both",
)
btn20.bind("<Enter>", enter20)
btn20.bind("<Leave>", left20)

data = StringVar()
lbl = Label(resultrow,
            text="Result",
            anchor=SE,
            height=8,
            font=("Veranda", 12),
            textvar=data)
lbl.pack(expand=True, fill="both")

# Functions
root_window.mainloop()
