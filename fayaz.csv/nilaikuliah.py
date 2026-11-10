import csv
FILE_NAME ='fayaz.csv/nilaikuliah.csv'
listnilai = []
with open(FILE_NAME) as csvFile:  
    # Melakukan parsing untuk pembacaan seluruh baris
    readCSV = csv.reader(csvFile, delimiter=';')
    line_count = 0

    # Melakukan penyimpanan baris-baris data menjadi nested list
    for baris in readCSV:
        if line_count == 0:
            print(f'Nama Kolom : {baris}')
            # listNilai1.append(baris)
            line_count += 1
        else:
            print(baris)
            listnilai.append(baris)
            line_count += 1

    print(f'Total {line_count} baris')

csvFile.close()
print("isi nested list yang dibuat :")
print(listnilai)