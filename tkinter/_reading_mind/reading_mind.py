from tkinter import *
from tkinter.ttk import *
import time


global x

def progres():
    
    def vysledek():
        vysled = Tk()
        vysled.minsize(200, 150)
        vysled.maxsize(200, 120)
        vysled.title("výsledek")
        vysled.geometry("200x120+500+200")
        text_vysledek = Label(vysled, text = f"Je to jasné, tvá\nodpověď je {textik.get()}", font = ("Arial", 14)).place(relx=0.5, rely=0.3, anchor = "center")
        btn_ukončit = Button(vysled, text = "ukončit", command=exit).place(relx=0.5,rely=0.7, anchor="center")
    def start():
        tasks = 25
        x = 0
        while x < tasks:
            time.sleep(0.15)
            if x == 0:
                text.config(text="zpínání kamery")
            elif x == 5:
                text.config(text="skenování obličeje")
            elif x == 8:
                text.config(text="skenování mozku")
            elif x == 16:
                text.config(text="prohledávání myšlenek")
            elif x == 20:
                text.config(text="")
                text.config(text="        hledání odpovědi        ")

            bar["value"]+=4
            window.update_idletasks()
            x+=1
            if x == tasks:
                window.destroy()
                vysledek()

    window = Tk()
    window.minsize(270, 100)
    window.geometry("270x100+500+200")
    window.title("čtení mysli")
    cinnost = ""
    text = Label(window)
    text.config(text=cinnost)
    text.pack()

    bar = Progressbar(window, orient="horizontal", length=300)
    bar.pack(pady=10)
    global button
    button = Button(window, text="začít", command=start).pack()

    main_app.destroy()
    window.mainloop()

def nepovedlo_se():
    main_app.destroy()

    nepov = Tk()
    nepov.geometry("270x110+500+200")
    nepov.title("nezadal")
    nepov.resizable(False, False)

    textikek = Label(nepov, text="Úspěšně jsi selhal při zadávání\njednoduchého čísla.\nAsi by ses měl vrátit do 2.třídy!!!", font=("Liberation Sans", 12), justify=CENTER).pack()
    tlacitko = Button(nepov, text="vrátit se do 2.třídy", command=exit).pack(pady=10)

global je_to_cislo

def je_to_cislo(x):
    try:
        x = str(textik.get())
        x = int(x)
        if x >= 1 and x <= 100:
            progres()
    except ValueError:
        nepovedlo_se()

main_app = Tk()
main_app.minsize(220,100)
main_app.maxsize(220,100)
main_app.title("zadej")
main_app.geometry("220x100+500+200")

text = Label(main_app, text="zadej číslo od 1 do 100", font=("Liberation Sans", 12)).place(rely=0.25, relx=0.5, anchor="center")
global textik
textik = StringVar()
textinput = Entry(main_app, textvariable=textik).place(rely=0.5, relx=0.5, anchor="center")
btn = Button(main_app, text="přečíst myšlenky", command = lambda: je_to_cislo(textik)).place(relx=0.5, rely=0.75, anchor="center")

main_app.mainloop()