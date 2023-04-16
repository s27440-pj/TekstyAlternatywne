import csv
import pandas as pd
import os
import sys

user = os.getlogin()

# Otwieramy plik CSV i wczytujemy jego zawartość
with open(f"C:/Users/{user}/Documents/tabela2.csv", 'r') as file:
    reader = csv.reader(file, delimiter=';')
    table_data = []
    table_headers = []
    for row in reader:
        # Jeśli wiersz zawiera dane, dodajemy go do bieżącej tabeli
        if any(row):
            table_data.append(row)
        # W przeciwnym razie tworzymy nową tabelę i zapisujemy nagłówki bieżącej tabeli
        else:
            if table_data:
                # dodanie opcji inplace=True nie pomaga
                table = pd.DataFrame(table_data[1:], columns=table_data[0]).dropna(how='all', axis=1)
                # Tabele zapisują się w końcu dobrze, ale liczba kolumn jest większa niż rzeczywista, mimo że powinny
                # się usuwać te puste?
                headlines = table.columns
                # print(headlines) - wyświetla się 8 kolumn (tyle ile jest w najszerszej tabeli) :( a ja chce 5
                columns = headlines.size
                # print(columns) - wyświetla się 8
                rows = table.index.size
                for i in range(0, rows):
                    for j in range(0, columns):
                        if j == 0:
                            option = str(table.loc[i, headlines[j]] + ": ")
                            sys.stdout.write(option)
                        elif j == columns - 1:
                            result = str(headlines[j] + " " + table.loc[i, headlines[j]] + ";")
                            sys.stdout.write(result)
                        else:
                            result = str(headlines[j] + " " + table.loc[i, headlines[j]] + ", ")
                            sys.stdout.write(result)
                    print()
            table_headers.append(table_data)
            table_data = []
    # Ostatnią tabelę należy dodać poza pętlą for
    if table_data:
        table = pd.DataFrame(table_data[1:], columns=table_data[0]).dropna(how='all', axis=1)
        headlines = table.columns
        columns = headlines.size
        rows = table.index.size
        for i in range(0, rows):
            for j in range(0, columns):
                if j == 0:
                    option = str(table.loc[i, headlines[j]] + ": ")
                    sys.stdout.write(option)
                elif j == columns - 1:
                    result = str(headlines[j] + " " + table.loc[i, headlines[j]] + ";")
                    sys.stdout.write(result)
                else:
                    result = str(headlines[j] + " " + table.loc[i, headlines[j]] + ", ")
                    sys.stdout.write(result)
            print()
