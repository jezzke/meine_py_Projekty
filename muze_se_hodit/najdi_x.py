text = input('Zkopírujte text a vložte ho sem: ')
x = input('Zadejte hledaný znak: ')
pozice = 0
for znak in text:
    pozice += 1
    if str(znak) == str(x):
        print(pozice)

