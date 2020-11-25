
#import bibliotek
import numpy as np
import csv
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
#zmienne
v_fali =4500

def wczytanie_stanowisk():
    poprawne_wczytanie = False
    while poprawne_wczytanie == False:
        try:
            stanowiska = np.loadtxt('data/stanowiska.csv', delimiter=';', skiprows=1)
            poprawne_wczytanie = True
        except OSError as e:
            print("Błąd wczytania pliku, spróbuj jeszcze raz ")
    return stanowiska

def wczytanie_wstrzasow():
    poprawne_wczytanie = False
    while poprawne_wczytanie == False:
        try:
            wstrzasy = np.loadtxt('data/dane.csv', delimiter=';', skiprows=1)
            poprawne_wczytanie = True
        except OSError as e:
            print("Błąd wczytania pliku, spróbuj jeszcze raz ")
    wstrzasy=wstrzasy/1000
    return wstrzasy
def matrixA(s,d,w):
    print("siema")
    a = np.zeros((7,4))
    for row in range(0,7):
        for col in range(0,4):
            if col != 3:
                a[row,col] = (2*(s[0,col]-d[row,col]))
            else :
                a[row,col] = (2*(d[row,1]-d[0,1])*v_fali)
    print(a)
        
Stanowiska= wczytanie_stanowisk() #s= stanowiska d=wstrzasy w=ilosc wstrzasow
Wstrzasy= wczytanie_wstrzasow()   
ilosc_wstrzasow = (Wstrzasy.shape[1])
for i in range(0,ilosc_wstrzasow):
    A= matrixA(Stanowiska,Wstrzasy,ilosc_wstrzasow)


