import csv
import pandas as pd
import os

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
                table = pd.DataFrame(table_data[1:], columns=table_data[0]).dropna(how='all', axis=1)
                print(table.head(5))
            table_headers.append(table_data)
            table_data = []
    # Ostatnią tabelę należy dodać poza pętlą for
    if table_data:
        table = pd.DataFrame(table_data[1:], columns=table_data[0]).dropna(how='all', axis=1)
        print(table.head(5))