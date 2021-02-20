# Program służy do lokalizacji ogniska wstrząsu górniczego na podstawie danych dostarczonych do 8 stanowisk
## Paweł Nalepka PolŚl GIBiAP semestr 3 gr 2 2020
# import bibliotek
import numpy as np
import easygui
import matplotlib.pyplot as plt

# zmienne
v_fali = 4500


def wczytanie_stanowisk():
    plik_stanowiska = easygui.fileopenbox(title='Wybierz plik stanowisk:')
    poprawne_wczytanie = False
    while poprawne_wczytanie == False:
        try:
            stanowiska = np.loadtxt(plik_stanowiska, delimiter=';', skiprows=1)
            poprawne_wczytanie = True
        except OSError as e:
            print("Błąd wczytania pliku, spróbuj jeszcze raz ")
    return stanowiska


def wczytanie_wstrzasow():
    plik_wstrzasu = easygui.fileopenbox('Wybierz plik danych:')
    poprawne_wczytanie = False
    while poprawne_wczytanie == False:
        # ruchampsahajsra
        try:
            wstrzasy = np.loadtxt(plik_wstrzasu, delimiter=';', skiprows=1)
            poprawne_wczytanie = True
        except OSError as e:
            print("Błąd wczytania pliku, spróbuj jeszcze raz ")
    wstrzasy = wstrzasy / 1000
    return wstrzasy


def matrixA(s, d, w):
    a = np.zeros((7, 4))
    for row in range(0, 7):
        for col in range(0, 4):
            if col != 3:
                a[row, col] = 2 * (s[0, col] - s[row + 1, col])
            else:
                a[row, col] = 2 * (d[row + 1, w] - d[0, w]) * (v_fali ** 2)
    return a


def matrixB(s, d, w):
    b = np.zeros((7, 1))
    # print (d)
    # print (w)
    for row in range(0, 7):
        b[row, 0] = (v_fali ** 2) * ((d[row + 1, w] ** 2) - (d[0, w] ** 2)) + (s[0, 0] ** 2) - (s[row + 1, 0] ** 2) + (
                s[0, 1] ** 2) - (s[row + 1, 1] ** 2) + (s[0, 2] ** 2) - (s[row + 1, 2] ** 2)
    return b


def wynik(a, b, w):
    AT = a.T
    macierzA = np.dot(AT, a)
    # print(macierzA)
    macierzB = np.dot(AT, b)
    # print(macierzB)
    wynik = np.linalg.solve(macierzA, macierzB)
    for row in range(0, 4):
        Tablicawyniku[row, w] = wynik[row, 0]
    return Tablicawyniku


def wydruk(tabela_wyniku, stanowiska):
    f = open('wynik.csv', "a")
    print(tabela_wyniku)
    np.savetxt('wynik.csv', tabela_wyniku, delimiter=';')
    wykres_stanowiska = stanowiska.T
    fig, ax = plt.subplots()
    ax.grid(True, which='both')
    plt.plot(tabela_wyniku[0:1], tabela_wyniku[1:2], marker='x')
    plt.plot(wykres_stanowiska[0:1], wykres_stanowiska[1:2], marker='o')
    plt.show()


if __name__ == ("__main__"):
    Stanowiska = wczytanie_stanowisk()  # s= stanowiska d=wstrzasy w=ilosc wstrzasow
    Wstrzasy = wczytanie_wstrzasow()
    ilosc_wstrzasow = (Wstrzasy.shape[1])

    Tablicawyniku = np.zeros((4, ilosc_wstrzasow))

    for i in range(0, ilosc_wstrzasow):
        A = matrixA(Stanowiska, Wstrzasy, i)
        B = matrixB(Stanowiska, Wstrzasy, i)
        do_druku = wynik(A, B, i)

    wydruk(do_druku, Stanowiska)
