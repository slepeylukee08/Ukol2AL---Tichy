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

import random

def bogo_sort(arr):
    def is_sorted(arr):
        return all(arr[i] <= arr[i+1] for i in range(len(arr) - 1))

    while not is_sorted(arr):
        random.shuffle(arr)
    return arr

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
#Test
if __name__ == "__main__":
    test_array = [random.randint(0, 100) for _ in range(10)]
    print("Original Array:", test_array)

    print("\nBogo Sort:", bogo_sort(test_array[:]))
    print("Selection Sort:", selection_sort(test_array[:]))
    print("Insertion Sort:", insertion_sort(test_array[:]))





