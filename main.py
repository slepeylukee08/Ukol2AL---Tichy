#Úkol 1 -  Vytvořte jednorozměrné pole, které bude mít 10 náhodných hodnot (0-100)
import random

# Vytvoření jednorozměrného pole s 10 náhodnými hodnotami mezi 0 a 100
random_array = [random.randint(0, 100) for _ in range(10)]

print(random_array) #Vypise nahodne cisla v nahodnem poradi v poli

#Úkol 2 - Vytvořte jednoduchý sort.

# Vytvoření jednorozměrného pole s 10 náhodnými hodnotami mezi 0 a 100
array = [random.randint(0, 100) for _ in range(10)]
print("Všechny vypsané pole, každý krok po sobě")

import random

def bubble_sort():
    n = len(array)
    for i in range(n-1):
        for j in range(0,n-i-1):
            if array[j] > array[j+1] : #Pokud je číslo napřílad na první pozici větší než druhé, tak to kód vyhodnotí a v dalším kroku to poté prohodí
                array[j], array[j+1] = array[j+1], array[j] # Prohození prvků
            print(array) #Výpis aktuálního stavu pole, vypíše se po každém kroku kódu, ikdyž se prohodí nebo ne
    return array

print(bubble_sort())





