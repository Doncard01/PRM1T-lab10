import os

def pierwsza(nazwa):
    slownik = {}
    files = os.listdir(os.path.abspath(nazwa))
    for file in files:
        if os.path.isdir(file):
            continue
        else:
            sciezka = os.path.splitext(file)
            rozmiar = os.path.getsize(os.path.abspath(nazwa + "\\" + file))
            slownik[sciezka[1]] = {sciezka[0]: rozmiar}

    return slownik
