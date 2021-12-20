import funkcje as f

katalog = "books"

if __name__ == '__main__':
    try:
        print(f.pierwsza(katalog))
    except (AssertionError, FileExistsError) as err:
        print("Błąd: ", err)
    try:
        f.druga(".txt", "books", "poe")
    except (AssertionError, FileExistsError) as err:
        print("Błąd: ", err)