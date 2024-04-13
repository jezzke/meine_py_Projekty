import tkinter as tk

app = tk.Tk()
app.title("převod měn")
app.geometry("238x130+400+120")
app.resizable(False, False)
app.config(bg="#1d4bc6")


# 1 euro == 25.29 czk
def eur_to_czk():
    try:
        tkL_vysledek.config(text=round(float(tkE_input.get()) * 25.29, 2))
    except ValueError:
        tkL_vysledek.config(text="Chyba")


def czk_to_eur():
    try:
        tkL_vysledek.config(text=round(float(tkE_input.get()) / 25.29, 2))
    except ValueError:
        tkL_vysledek.config(text="Chyba")


def reverse(smer):
    if smer == "z czk":
        tkB_prevod.config(command=lambda: eur_to_czk())
        tkB_reverse.config(command=lambda: reverse("z eur"))
        tkL_czk.grid_configure(row=1)
        tkL_eur.grid_configure(row=0)
        tkE_input.delete(0, tk.END)
        tkL_vysledek.config(text="")
    elif smer == "z eur":
        tkB_prevod.config(command=lambda: czk_to_eur())
        tkB_reverse.config(command=lambda: reverse("z czk"))
        tkL_czk.grid_configure(row=0)
        tkL_eur.grid_configure(row=1)
        tkE_input.delete(0, tk.END)
        tkL_vysledek.config(text="")


# wingets
tkL_czk = tk.Label(app, text="CZK", font=("Helvetica", 20, "bold"), bg="#1d4bc6", fg="#f5f9ff")
tkL_czk.grid(row=0, column=0, padx=(15, 10))
tkL_eur = tk.Label(app, text="EUR", font=("Helvetica", 20, "bold"), bg="#1d4bc6", fg="#f5f9ff")
tkL_eur.grid(row=1, column=0)
tkL_vysledek = tk.Label(app, text="0", font=("Helvetica", 14), bg="#1d4bc6", fg="#f5f9ff")
tkL_vysledek.grid(row=1, column=1)

tkE_input = tk.Entry(app, width=10, )
tkE_input.focus()
tkE_input.grid(row=0, column=1)

tkB_prevod = tk.Button(app, text="převod", command=lambda: czk_to_eur())
tkB_prevod.grid(row=0, column=2, padx=15, pady=15)
tkB_reverse = tk.Button(app, text="převrátit", command=lambda: reverse("z czk"))
tkB_reverse.grid(row=1, column=2)
app.mainloop()
