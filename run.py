
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
                a[row,col]=2*(s[0,col]-s[row+1,col])   
            else :
                a[row,col]=2*(d[row+1,w]-d[0,w])*(v_fali**2)
    return a              
def matrixB(s,d,w):
    print("siemaB")  
    b= np.zeros((7,1))
    for row in range(0,7):
        b[row,0]= (v_fali**2)*((d[row+1,w]**2)-(d[0,w]**2))+(s[0,0]**2)-(s[row+1,0]**2)+(s[0,1]**2)-(s[row+1,1]**2)+(s[0,2]**2)-(s[row+1,2]**2)
    return b
def wynik(a,b,w):
    odwrotnosc= np.matmul(a.T,a)
    odwrotnosc = odwrotnosc**(-1)
    ATB= np.matmul(odwrotnosc,a.T)
    Wynik=np.matmul(ATB,b)
    print("no kurwa no ")
    print(Wynik)
    print("no kurwa no ")
    
    
Stanowiska= wczytanie_stanowisk() #s= stanowiska d=wstrzasy w=ilosc wstrzasow
Wstrzasy= wczytanie_wstrzasow()   
ilosc_wstrzasow = (Wstrzasy.shape[1])
print(Stanowiska)
print("xDDDDDDDDDDDD")
print(Wstrzasy)
for i in range(0,ilosc_wstrzasow):
    A= matrixA(Stanowiska,Wstrzasy,i)
    B= matrixB(Stanowiska,Wstrzasy,i)
    Elo = wynik(A,B,i)
