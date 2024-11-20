#Úkol 1 -  Vytvořte jednorozměrné pole, které bude mít 10 náhodných hodnot (0-100)
import random

# Vytvoření jednorozměrného pole s 10 náhodnými hodnotami mezi 0 a 100
random_array = [random.randint(0, 100) for _ in range(10)]

print(random_array) #Vypise nahodne cisla v nahodnem poradi v poli

#2 - Vytvořte jednoduchý sort.

# Vytvoření jednorozměrného pole s 10 náhodnými hodnotami mezi 0 a 100
random_array = [random.randint(0, 100) for _ in range(10)]

# Bubble Sort - jednoduché třídění
for i in range(len(random_array)):    #Cyklus bude probíhat tolikrát, kolik je prvků v poli random_array, promenna i bude nabyvat hodnotu od 0 do delky pole -1
        if random_array[j] > random_array[j + 1]: #Cyklus prochází polem od indexu 0 až do indexu len(random_array) - i - 1
            random_array[j], random_array[j + 1] = random_array[j + 1], random_array[j] #Tohle znamená že dochází k promeně nebo výměně hodnot na určené pozicích j a j + 1 v poli random_array

# Výpis výsledků
print("Náhodné pole:", random_array)

