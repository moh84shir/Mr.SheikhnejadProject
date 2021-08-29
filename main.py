from tkinter import *
import tkinter.messagebox


def shetab():
    window_shetab = Tk()
    window_shetab.title("محاسبه کننده ی شتاب")
    window_shetab.resizable(width=False, height=False)

    LabelN = Label(window_shetab, text=': نیرو ی خالص ')
    LabelN.grid(row=0, column=1)

    Ntext = StringVar()
    EntryN = Entry(window_shetab, textvariable=Ntext)
    EntryN.grid(row=0, column=0)

    LabelG = Label(window_shetab, text=': جرم جسم ')
    LabelG.grid(row=1, column=1)

    Gtext = StringVar()
    EntryG = Entry(window_shetab, textvariable=Gtext)
    EntryG.grid(row=1, column=0)

    bShet = Button(window_shetab, text="شتاب را محاسبه کن",
                   command=lambda: shet())
    bShet.grid(row=2, column=0)

    def shet():
        try:
            tkinter.messagebox._show(
                "شتاب", f"{float(EntryN.get()) / float(EntryG.get())}")

        except:
            tkinter.messagebox.showerror('مشکل', 'مشکلی وجود دارد. لطفا مقادیر وارد شده را بررسی کنید')


    window_shetab.mainloop()


def baraiand():
    window_baraiand = Tk()
    window_baraiand.title("محاسبه کننده ی برایند")
    window_baraiand.resizable(width=False, height=False)

    LabelG1 = Label(window_baraiand, text=': نیرو ی اول ')
    LabelG1.grid(row=0, column=1)

    G1text = StringVar()
    EntryG1 = Entry(window_baraiand, textvariable=G1text)
    EntryG1.grid(row=0, column=0)

    LabelG2 = Label(window_baraiand, text=': نیرو ی دوم  ')
    LabelG2.grid(row=1, column=1)

    G2text = StringVar()
    EntryG2 = Entry(window_baraiand, textvariable=G2text)
    EntryG2.grid(row=1, column=0)

    bShet = Button(window_baraiand, text="برایند را محاسبه کن",
                   command=lambda: bara())
    bShet.grid(row=2, column=0)

    def bara():
        try:
            tkinter.messagebox._show(
                "برایند", f"{abs(abs(float(EntryG1.get())) - abs(float(EntryG2.get())))}")

        except:
            tkinter.messagebox.showerror('مشکل', 'مشکلی وجود دارد. لطفا مقادیر وارد شده را بررسی کنید')

    window_baraiand.mainloop()


def gashtavar():

    window_gashtavar = Tk()
    window_gashtavar.title("محاسبه کننده ی گشتاور")
    window_gashtavar.resizable(width=False, height=False)

    LabelG = Label(window_gashtavar, text=': نیرو ')
    LabelG.grid(row=0, column=1)

    Gtext = StringVar()
    EntryG = Entry(window_gashtavar, textvariable=Gtext)
    EntryG.grid(row=0, column=0)

    LabelM = Label(window_gashtavar, text=': فاصله اثر نیرو تا محور چرخش  ')
    LabelM.grid(row=1, column=1)

    Mtext = StringVar()
    EntryM = Entry(window_gashtavar, textvariable=Mtext)
    EntryM.grid(row=1, column=0)

    bShet = Button(window_gashtavar, text="گشتاور را محاسبه کن",
                   command=lambda: gash())
    bShet.grid(row=2, column=0)

    def gash():
        try:
            tkinter.messagebox._show(
                "گشتاور", f"{float(EntryG.get()) * float(EntryM.get())}")

        except:
            tkinter.messagebox.showerror('مشکل', 'مشکلی وجود دارد. لطفا مقادیر وارد شده را بررسی کنید')

    window_gashtavar.mainloop()


window = Tk()

b1 = Button(window, text='محاسبه کننده ی شتاب', command=lambda: shetab())
b1.grid()

b2 = Button(window, text='محاسبه کننده ی برایند', command=lambda: baraiand())
b2.grid(row=1)

b3 = Button(window, text='محاسبه کننده ی گشتاور ', command=lambda: gashtavar())
b3.grid(row=2)

window.resizable(width=False, height=False)


window.mainloop()
