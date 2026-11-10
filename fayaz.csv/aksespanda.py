import pandas as pd

FILECSV = 'fayaz.csv/nilaikuliah.csv'

dfCSV = pd.read_csv(FILECSV, delimiter=',', encoding='latin1')
print(dfCSV.head(7))