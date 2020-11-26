
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
    #print("siema")
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
    print (d)
    print (w)
    for row in range(0,7):
        b[row,0]= (v_fali**2)*((d[row+1,w]**2)-(d[0,w]**2))+(s[0,0]**2)-(s[row+1,0]**2)+(s[0,1]**2)-(s[row+1,1]**2)+(s[0,2]**2)-(s[row+1,2]**2)
    print("to jest macierz B")
    #print(w)
    print(b)
    print("kkurw")
    return b
def wynik(a,b,w):
    AT=a.T
    macierzA = np.dot(AT,a)
    macierzB = np.dot(AT,b)
    wynik = np.linalg.solve(macierzA, macierzB)
    #print("no kurwa no ")
    print(wynik)
    #print("no kurwa no ")
    
    for row in range(0,4):
        Tablicawyniku[row,w]=wynik[row,0]
    print(Tablicawyniku)
    
Stanowiska= wczytanie_stanowisk() #s= stanowiska d=wstrzasy w=ilosc wstrzasow
Wstrzasy= wczytanie_wstrzasow()   
ilosc_wstrzasow = (Wstrzasy.shape[1])
print(Stanowiska)
print("xDDDDDDDDDDDD")
print(Wstrzasy)
Tablicawyniku= np.zeros((4,ilosc_wstrzasow))
for i in range(0,ilosc_wstrzasow):
    A= matrixA(Stanowiska,Wstrzasy,i)
    B= matrixB(Stanowiska,Wstrzasy,i)
    Elo = wynik(A,B,i)
