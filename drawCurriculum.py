from tkinter import *
from turtle import *
from tkinter.ttk import Combobox
from curriculum import *

def RightFrames():
    Rightframe1 = Frame(RightMayFrame)
    foto = PhotoImage(file='C:/Users/mike/PycharmProjects/Curriculum vitae/Foto_Mike.gif')
    label = Button(Rightframe1, image=foto)
    label.image = foto
    label.pack()
    Rightframe1.grid(column=0, row=0)

    Rightframe2 = Frame(RightMayFrame, bd=8, relief=RAISED)
    Rightframe2.grid(column=0, row=1)
    GegevensLabel1 = Label(Rightframe2, text=Naam, anchor=W, relief=SUNKEN)
    GegevensLabel1.grid()
    GegevensLabel2 = Label(Rightframe2, text=Leeftijd, anchor=W, relief=SUNKEN)
    GegevensLabel2.grid()
    GegevensLabel2 = Label(Rightframe2, text=Adres, anchor=W, relief=SUNKEN)
    GegevensLabel2.grid()
    GegevensLabel2 = Label(Rightframe2, text=GSM, anchor=W, relief=SUNKEN)
    GegevensLabel2.grid()
    GegevensLabel2 = Label(Rightframe2, text=E_Mail, anchor=W, relief=SUNKEN)
    GegevensLabel2.grid()
    GegevensLabel2 = Label(Rightframe2, text=Geboorte, anchor=W, relief=SUNKEN)
    GegevensLabel2.grid()
    GegevensLabel2 = Label(Rightframe2, text=Nationaliteit, anchor=W, relief=SUNKEN)
    GegevensLabel2.grid()
    GegevensLabel2 = Label(Rightframe2, text=Rijbewijs, anchor=W, relief=SUNKEN)
    GegevensLabel2.grid()
    GegevensLabel2 = Label(Rightframe2, text=Hobbys, anchor=W, relief=SUNKEN)
    GegevensLabel2.grid()

    Rightframe3 = Frame(RightMayFrame, height=100, bd=8, relief=SUNKEN)
    Rightframe3.grid(column=0, row=2)

def school(event):
    for widget in LowerMayFrame2.winfo_children():
        widget.destroy()
    frame1 = Frame(LowerMayFrame2, width=25, bd=8)
    frame1.grid(row=0, column=0)

    frame2 = Frame(LowerMayFrame2, width=25, bd=8)
    frame2.grid(row=0, column=1)

    frame3 = Frame(LowerMayFrame2, width=25, bd=8)
    frame3.grid(row=0, column=2)

    frame4 = Frame(LowerMayFrame2, width=25, bd=8)
    frame4.grid(row=0, column=3)

    for f in School:
        f = Label(frame1, text=f, width=25, bd=8)
        f.grid(column=0)
#   for s in Jaren:
#       s = Label(frame2, text=str(s), width=25, bd=8)
#       s.grid(column=1)
    for a in Richtingen:
        a = Label(frame3, text=a, width=30, bd=8)
        a.grid(column=2)
    for r in Diplomas:
        r = Label(frame4, text=r, width=20, bd=8)
        r.grid(column=3)


def Computervaardigheden(event):
    for widget in LowerMayFrame2.winfo_children():
        widget.destroy()
    frame1 = Frame(LowerMayFrame2, width=50, bd=8, relief=RAISED)
    frame1.grid(row=0, column=0)
    label1 = Label(frame1, text=Vaardigheid1.programma, width=50, bd=8)
    label1.grid(row=0, column=0)
    box1 = Combobox(frame1, width=50)
    box1["values"] = ("Zeer goed", "Goed", "Basis")
    box1.set("zeer goed")
    box1.grid(row=0, column=1)


    frame2 = Frame(LowerMayFrame2, width=50, bd=8, relief=SUNKEN)
    frame2.grid(row=1, column=0)
    label2 = Label(frame2, text=Vaardigheid2.programma, width=50, bd=8)
    label2.grid(row=1, column=0)
    box2 = Combobox(frame2, width=50)
    box2["values"] = ("Zeer goed", "Goed", "Basis")
    box2.set("goed")
    box2.grid(row=1, column=1)

    frame3 = Frame(LowerMayFrame2, width=50, bd=8, relief=RAISED)
    frame3.grid(row=2, column=0)
    label3 = Label(frame3, text=Vaardigheid3.programma, width=50, bd=8)
    label3.grid(row=2, column=0)
    box3 = Combobox(frame3, width=50)
    box3["values"] = ("Zeer goed", "Goed", "Basis")
    box3.set("goed")
    box3.grid(row=2, column=1)

    frame4 = Frame(LowerMayFrame2, width=50, bd=8, relief=SUNKEN)
    frame4.grid(row=3, column=0)
    label4 = Label(frame4, text=Vaardigheid4.programma, width=50, bd=8)
    label4.grid(row=3, column=0)
    box4 = Combobox(frame4, width=50)
    box4["values"] = ("Zeer goed", "Goed", "Basis")
    box4.set("goed")
    box4.grid(row=3, column=1)

    frame5 = Frame(LowerMayFrame2, width=50, bd=8, relief=RAISED)
    frame5.grid(row=4, column=0)
    label5 = Label(frame5, text=Vaardigheid5.programma, width=50, bd=8)
    label5.grid(row=4, column=0)
    box5 = Combobox(frame5, width=50)
    box5["values"] = ("Zeer goed", "Goed", "Basis")
    box5.set("goed")
    box5.grid(row=4, column=1)

    frame6 = Frame(LowerMayFrame2, width=50, bd=8, relief=SUNKEN)
    frame6.grid(row=5, column=0)
    label6 = Label(frame6, text=Vaardigheid6.programma, width=50, bd=8)
    label6.grid(row=5, column=0)
    box6 = Combobox(frame6, width=50)
    box6["values"] = ("Zeer goed", "Goed", "Basis")
    box6.set("goed")
    box6.grid(row=5, column=1)

    frame7 = Frame(LowerMayFrame2, width=50, bd=8, relief=RAISED)
    frame7.grid(row=6, column=0)
    label7 = Label(frame7, text=Vaardigheid7.programma, width=50, bd=8)
    label7.grid(row=6, column=0)
    box7 = Combobox(frame7, width=50)
    box7["values"] = ("Zeer goed", "Goed", "Basis")
    box7.set("Basis")
    box7.grid(row=6, column=1)

    frame8 = Frame(LowerMayFrame2, width=50, bd=8, relief=SUNKEN)
    frame8.grid(row=7, column=0)
    label8 = Label(frame8, text=Vaardigheid8.programma, width=50, bd=8)
    label8.grid(row=7, column=0)
    box8 = Combobox(frame8, width=50)
    box8["values"] = ("Zeer goed", "Goed", "Basis")
    box8.set("Basis")
    box8.grid(row=7, column=1)

    frame9 = Frame(LowerMayFrame2, width=50, bd=8, relief=RAISED)
    frame9.grid(row=8, column=0)
    label9 = Label(frame9, text=Vaardigheid9.programma, width=50, bd=8)
    label9.grid(row=8, column=0)
    box9 = Combobox(frame9, width=50)
    box9["values"] = ("Zeer goed", "Goed", "Basis")
    box9.set("Basis")
    box9.grid(row=8, column=1)

    frame10 = Frame(LowerMayFrame2, width=50, bd=8, relief=SUNKEN)
    frame10.grid(row=9, column=0)
    label10 = Label(frame10, text=Vaardigheid10.programma, width=50, bd=8)
    label10.grid(row=9, column=0)
    box10 = Combobox(frame10, width=50)
    box10["values"] = ("Zeer goed", "Goed", "Basis")
    box10.set("Basis")
    box10.grid(row=9, column=1)

    frame11 = Frame(LowerMayFrame2, width=50, bd=8, relief=RAISED)
    frame11.grid(row=10, column=0)
    label11 = Label(frame11, text=Vaardigheid11.programma, width=50, bd=8)
    label11.grid(row=10, column=0)
    box11 = Combobox(frame11, width=50)
    box11["values"] = ("Zeer goed", "Goed", "Basis")
    box11.set("Basis")
    box11.grid(row=10, column=1)


def TaalVaardigheden(event):
    for widget in LowerMayFrame2.winfo_children():
        widget.destroy()
    label0 = Label(LowerMayFrame2,
                   text=("+-------Taal----------+", "+---------Lezen-------+", "+------Schrijven------+",
                         "+------Spreken--------+"), width=100, bd=8, relief=RAISED)
    label0.pack()

    label1 = Label(LowerMayFrame2,
                   text=(Taal_vaardigheden.Taal[0], Taal_vaardigheden.Lezen[0], Taal_vaardigheden.Schrijven[0],
                                        Taal_vaardigheden.Spreken[0]))
    label1.pack(side=TOP)

    label2 = Label(LowerMayFrame2,
                       text=(Taal_vaardigheden.Taal[1], Taal_vaardigheden.Lezen[1], Taal_vaardigheden.Schrijven[1],
                         Taal_vaardigheden.Spreken[1]), bd=8)
    label2.pack(side=TOP)

    label3 = Label(LowerMayFrame2,
                       text=(Taal_vaardigheden.Taal[2], Taal_vaardigheden.Lezen[4], Taal_vaardigheden.Schrijven[4],
                         Taal_vaardigheden.Spreken[4]), bd=8)
    label3.pack(side=TOP)

    label4 = Label(LowerMayFrame2,
                     text=(Taal_vaardigheden.Taal[3], Taal_vaardigheden.Lezen[5], Taal_vaardigheden.Schrijven[5],
                         Taal_vaardigheden.Spreken[5]), bd=8)
    label4.pack(side=TOP)


def Werkervaring(event):
    for widget in LowerMayFrame2.winfo_children():
        widget.destroy()
    label1 = Label(LowerMayFrame2, text=(Werkervaring1.werkgever, Werkervaring1.jaar, Werkervaring1.jaar_eind,
                                         Werkervaring1.job_inhoud), width=100, bd=8)

    label1.pack()
    label2 = Label(LowerMayFrame2, text=(Werkervaring2.werkgever, Werkervaring2.jaar, Werkervaring2.jaar_eind,
                                         Werkervaring2.job_inhoud), width=100, bd=8)
    label2.pack()
    label3 = Label(LowerMayFrame2, text=(Werkervaring3.werkgever, Werkervaring3.jaar, Werkervaring3.jaar_eind,
                                         Werkervaring1.job_inhoud), width=100, bd=8)
    label3.pack()
    label4 = Label(LowerMayFrame2, text=(Werkervaring4.werkgever, Werkervaring4.jaar, Werkervaring4.jaar_eind,
                                         Werkervaring1.job_inhoud), width=100, bd=8)
    label4.pack()
    label5 = Label(LowerMayFrame2, text=(Werkervaring5.werkgever, Werkervaring5.jaar, Werkervaring5.jaar_eind,
                                         Werkervaring1.job_inhoud), width=100, bd=8)
    label5.pack()
    label6 = Label(LowerMayFrame2, text=(Werkervaring6.werkgever, Werkervaring6.jaar, Werkervaring6.jaar_eind,
                                         Werkervaring1.job_inhoud), width=100, bd=8)
    label6.pack()
    label7 = Label(LowerMayFrame2, text=(Werkervaring7.werkgever, Werkervaring7.jaar, Werkervaring7.jaar_eind,
                                         Werkervaring1.job_inhoud), width=100, bd=8)
    label7.pack()
    label8 = Label(LowerMayFrame2, text=(Werkervaring8.werkgever, Werkervaring8.jaar, Werkervaring8.jaar_eind,
                                         Werkervaring1.job_inhoud), width=100, bd=8)
    label8.pack()

root1 = Tk()

root1.title("Curriculum vitae")
root1.configure(background="black")
LeftMayFrame = Frame(root1, width=1000, height=650, bd=8, relief="raise")
LeftMayFrame.pack(side=LEFT)
RightMayFrame = Frame(root1, width=350, height=630, bd=8, relief="raise")
RightMayFrame.pack(side=RIGHT)

UpperMayFrame = Frame(LeftMayFrame, width=1000, height=50, bd=8, relief="raise", bg="blue")
UpperMayFrame.pack(side=TOP)

menu = Menu(root1)
root1.config(menu=menu)
subMenu = Menu(menu)
menu.add_cascade(label="file", menu=subMenu)
subMenu.add_command(label="reset", command="ClearFrame")
subMenu.add_separator()
subMenu.add_command(label="Exit", command=root1.quit)

editMenu = Menu(menu)
menu.add_cascade(label="edit", menu=editMenu)
editMenu.add_command(label="redo", command="ClearFrame()")

LowerMayFrame = Frame(LeftMayFrame, width=1000, height=600, bd=8, relief="raise")
LowerMayFrame.pack(side=TOP)

LowerMayFrame1 = Frame(LowerMayFrame, width=200, height=600, bd=8, relief=SUNKEN)
LowerMayFrame1.pack(side=LEFT)
LowerMayFrame2 = Frame(LowerMayFrame, width=800, height=600, bd=8, relief=SUNKEN)
LowerMayFrame2.pack(side=RIGHT)

printButton1 = Button(LowerMayFrame1, text="Opleidingen", command="school()", width=40, height=10, bd=8)
printButton1.bind('<Button-1>', school)
printButton1.grid(row=2, column=1)

printButton2 = Button(LowerMayFrame1, text="Werkervaringen", command="werkervaring()", width=40, height=10, bd=8)
printButton2.bind('<Button-1>', Werkervaring)
printButton2.grid(row=3, column=1)

printButton3 = Button(LowerMayFrame1, text="Computer vaardigheden", command="computervaardigheden()", width=40,
                      height=10, bd=8)
printButton3.bind('<Button-1>', Computervaardigheden)
printButton3.grid(row=4, column=1)
printButton4 = Button(LowerMayFrame1, text="Talen", command="taal", width=40, height=10, bd=8)
printButton4.bind('<Button-1>', TaalVaardigheden)
printButton4.grid(row=5, column=1)

quitButton = Button(UpperMayFrame, text="QUIT", command=root1.quit)
quitButton.pack(side=RIGHT, fill=X)

RightFrames()


root1.mainloop()