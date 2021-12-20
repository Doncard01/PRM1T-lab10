import os

def pierwsza(nazwa):
    assert isinstance(nazwa, str), "Podany parametr nie jest napisem!"
    assert len(nazwa) != 0, "Podaj niepustą nazwę pliku!"
    if os.path.exists(os.path.abspath(nazwa)) == False:
        raise FileExistsError("Nie znaleziono katalogu!")
    slownik = {}
    files = os.listdir(os.path.abspath(nazwa))
    for file in files:
        if os.path.isfile(nazwa + "\\" + file):
            sciezka = os.path.splitext(file)
            rozmiar = os.path.getsize(os.path.abspath(nazwa + "\\" + file))
            slownik[sciezka[1]] = {sciezka[0]: rozmiar}
        else:
            continue

    return slownik
