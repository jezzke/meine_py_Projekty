import random
import os

listik = ["Tichý oceán", 'Atlantský oceán', 'Indický oceán', 'Severní ledový oceán', 'Kaspické moře', 'Černé moře', 'Středozemní moře', 'Arabské moře', 'Jihočínské moře', "Filipínské moře", 'Barentsovo moře', 'Sargasové moře', 'Beaufortovo moře', 'Severní moře', 'Weddellovo moře', 'Korálové moře', 'Tasmanovo moře']

repeat = 17

clear = lambda: os.system('cls')
clear()

while repeat > 0:
    repeat -= 1
    picked = random.randint(0, repeat)
    print(listik.pop(picked))
    input("")
    clear()

