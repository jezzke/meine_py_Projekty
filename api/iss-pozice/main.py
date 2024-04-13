import requests
import tkinter as tk


app = tk.Tk()
app.geometry("200x80+300+100")
app.resizable(False, False)
app.title("ISS")


# funkce
def iss_geo_get():
    responce = requests.get("http://api.open-notify.org/iss-now.json")
    responce.raise_for_status()
    data = responce.json()
    sirka = data["iss_position"]["latitude"]
    vyska = data["iss_position"]["longitude"]
    tkL_sirka.config(text=f"šířka je {sirka}")
    tkL_vyska.config(text=f"výška je {vyska}")

# frame
tkF_frame = tk.Frame(app)
tkF_frame.pack()

# button
tkB_recount = tk.Button(tkF_frame, text="současné souřadnice ISS", command=iss_geo_get)
tkB_recount.pack()

# label
tkL_sirka = tk.Label(app)
tkL_sirka.pack()
tkL_vyska = tk.Label(app)
tkL_vyska.pack()


app.mainloop()
