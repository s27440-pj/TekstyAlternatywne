# This code will read csv/Excel file, containing a chart data, into a data frame.
# Next, it will create alternative text.
# Ultimately it should read multiple tables from a file and put each table into
# a different data frame, but I plan to upgrade it in the future.
import sys
import pandas as pd
import os

user = os.getlogin()

table = pd.read_csv(f"C:/Users/{user}/Documents/tabela.csv", delimiter=';')

# saving headlines into a list(?) - I can call now headlines[i]
headlines = table.columns
columns = headlines.size
rows = table.index.size
for i in range(0, rows):
    for j in range(0, columns):
        if j == 0:
            option = (table.loc[i, headlines[j]] + ": ")
            sys.stdout.write(option)
        elif j == columns - 1:
            result = (headlines[j] + " " + table.loc[i, headlines[j]] + ";")
            sys.stdout.write(result)
        else:
            result = (headlines[j] + " " + table.loc[i, headlines[j]] + ", ")
            sys.stdout.write(result)
    print()
