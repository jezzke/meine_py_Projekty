import tkinter as tk
import requests

# Okno
app = tk.Tk()
app.geometry("300x300+400+100")
app.title('aplikace na urážky')
app.config(bg="#192F43")

# colors and customization
cc_bg = '#192F43'
cc_bg2 = '#A8CCED'
cc_fg = '#E0F0FF'
cc_fg2 = '#17446E'
cf_n = ('Helvetika', 14, 'bold')
cf_s = ('Helvetika', 10, 'bold')


# Funkce
def insult_me():
    parameters = {"lang": 'en',
                  "type": "json"}
    responce = requests.get("https://evilinsult.com/generate_insult.php", params=parameters)
    responce.raise_for_status()
    data = responce.json()
    tkL_insult.config(text=data["insult"])


# Tlačítko
tkB_insult = tk.Button(app, text="najít urážku", font=cf_s, fg=cc_bg, bg=cc_bg2,  command=insult_me)
tkB_insult.place(relx=0.5, rely=0.1, anchor='center')

# Label
tkL_insult = tk.Label(app, wraplength=250, font=cf_n, bg=cc_bg, fg=cc_fg)
tkL_insult.place(relx=0.5, rely=0.5, anchor='center')

# hlavní cyklus
app.mainloop()
