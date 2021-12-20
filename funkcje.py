import os
import shutil

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
            if sciezka[1] in slownik.keys():
                slownik[sciezka[1]].update({sciezka[0]: rozmiar})
            else:
                slownik[sciezka[1]] = {sciezka[0]: rozmiar}
        else:
            katalog = nazwa + "\\" + file
            slownik = pierwsza(katalog)
    return slownik

def druga(rozszerzenie, skad, do):
    assert isinstance(rozszerzenie, str), "Podany parametr <rozszerzenie> nie jest napisem!"
    assert isinstance(skad, str), "Podany parametr <skad> nie jest napisem!"
    assert isinstance(do, str), "Podany parametr <do> nie jest napisem!"
    if os.path.exists(os.path.abspath(skad)) == False or os.path.exists(os.path.abspath(do)) == False:
        raise FileExistsError("Nie znaleziono katalogu!")
    files = os.listdir(os.path.abspath(skad))
    for file in files:
        src = os.path.join(skad, file)
        des = os.path.abspath(do)
        if rozszerzenie == os.path.splitext(file)[1]:
            if os.path.isdir(do) == False:
                os.makedirs(des)

            shutil.copyfile(src, des)