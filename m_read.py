import csv

def read_base_and_display(file_csv, fieldnames): # Вывод списка на экран
    with open(file_csv, encoding='utf8', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        print('')
        for row in reader:
            print(row[fieldnames[0]], row[fieldnames[1]], row[fieldnames[2]],  row[fieldnames[3]], 
                row[fieldnames[4]], row[fieldnames[5]], row[fieldnames[6]], row[fieldnames[7]], 
                row[fieldnames[8]])
        print('')