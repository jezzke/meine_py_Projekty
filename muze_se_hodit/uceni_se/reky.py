import random
import os

listik = ["Amazonka", "Nil", "Volha", "Rýn", "Ganga", "Žlutá řeka", "Kongo", "Darling", "Mississippi", "Rio Grande", "Paraná", "Zambezi", "Dunaj", "Ob", "ř. sv. Vavřince"]

repeat = 15

clear = lambda: os.system('cls')
clear()

while repeat > 0:
    repeat -= 1
    picked = random.randint(0, repeat)
    print(listik.pop(picked))
    input("")
    clear()

