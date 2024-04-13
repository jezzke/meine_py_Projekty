import tkinter as tk
import customtkinter

# okno
app = customtkinter.CTk()
app.title("TODO")
app.geometry("450x380+400+170")
app.resizable(False, False)

# definice barev
f_main = customtkinter.CTkFont(family="Helvetica", size=14,)
c_main = "#01347d"
c_button = "#b2d1fe"


# funkce
def add_text():
    tkT_todo.insert(tk.END, tkE_input.get())
    tkE_input.delete(0, tk.END)


def rm_text_item():
    tkT_todo.delete(tk.ANCHOR)


def rm_list_all():
    tkT_todo.delete(0, tk.END)


def save_list():
   # uloží úkoly do textového souboru
   with open("TODO.txt", "w") as file:
       my_tasks = tkT_todo.get(0, tk.END)
       for one_task in my_tasks:
           if one_task.endswith("\n"):
               file.write(f"{one_task}")
           else:
                file.write(f"{one_task}\n")



def load_tasks():
   try:
       with open("TODO.txt", "r") as file:
           for one_line in file:
               tkT_todo.insert(tk.END, one_line)
   except:
       pass


# framy
tkF_input = customtkinter.CTkFrame(app)
tkF_input.pack(pady=(10, 5))
tkF_text = customtkinter.CTkFrame(app)
tkF_text.pack()
tkF_buttons = customtkinter.CTkFrame(app)
tkF_buttons.pack()


# input frame - obsah
tkE_input = customtkinter.CTkEntry(tkF_input, width=380, font=f_main, placeholder_text="write TODO things here")
tkE_input.focus()
tkE_input.grid(row=0, column=0, padx=(0, 6))
tkB_add = customtkinter.CTkButton(tkF_input, width=30, text="add", border_width=2, font=f_main, command=add_text)
tkB_add.grid(row=0, column=1, padx=(6, 0))

# text frame - obsah
tkSB_todoScroll = customtkinter.CTkScrollbar(tkF_text)
tkSB_todoScroll.grid(row=0, column=1, sticky=tk.N+tk.S)

tkT_todo = tk.Listbox(tkF_text, width=64, height=21, borderwidth=3, font=f_main, yscrollcommand=tkSB_todoScroll.set)
tkT_todo.grid(row=0, column=0)
tkSB_todoScroll.configure(command=tkT_todo.yview)

# button frame
vel = 102
btnpadx = 3
tkB_remove = customtkinter.CTkButton(tkF_buttons,text="remove", width=vel, font=f_main, command=rm_text_item)
tkB_remove.grid(row=0, column=0, pady=10, padx=btnpadx)
tkB_clear = customtkinter.CTkButton(tkF_buttons,text="clear", width=vel, font=f_main, command=rm_list_all)
tkB_clear.grid(row=0, column=1, pady=5, padx=btnpadx)
tkB_save = customtkinter.CTkButton(tkF_buttons,text="save", width=vel, font=f_main, command=save_list)
tkB_save.grid(row=0, column=2, pady=5, padx=btnpadx)
tkB_quit = customtkinter.CTkButton(tkF_buttons,text="quit", width=vel, font=f_main, command=exit)
tkB_quit.grid(row=0, column=3, pady=5, padx=btnpadx)


load_tasks()
# hlavní cyklus
app.mainloop()

#
