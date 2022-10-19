import csv
import re

def read_base_and_write_csv_file(file_csv, fieldnames):
    print('')
    with open('class.csv', encoding='utf8', newline='') as csvfile_in:
        reader = csv.DictReader(csvfile_in)
        with open(file_csv, 'a', encoding='utf8', newline='') as csvfile_out:
            writer = csv.DictWriter(csvfile_out, fieldnames=fieldnames)
            writer.writeheader()
            for row in reader:
                stroka = int(row['Класс']) + 1
                if row['Пометка_перевода'] != 'NONE':
                    liter = re.findall(r'[А-Д]+', row['Пометка_перевода'])
                    liter = liter[0]
                    klass = re.findall(r'\d+', row['Пометка_перевода'])
                    klass = klass[0]
                    row['Пометка_перевода'] = 'NONE'
                    writer.writerow({fieldnames[0]: row[fieldnames[0]], fieldnames[1]: row[fieldnames[1]], 
                        fieldnames[2]: row[fieldnames[2]], fieldnames[3]: row[fieldnames[3]], 
                        fieldnames[4]: f'{klass}', fieldnames[5]: f'{liter}', 
                        fieldnames[6]: row[fieldnames[6]], fieldnames[7]: row[fieldnames[7]], 
                        fieldnames[8]: row[fieldnames[8]]})
                    print(f'{row[fieldnames[1]]} {row[fieldnames[2]]} {row[fieldnames[3]]} перевелся в {klass}{liter} класс')    
                elif stroka == 12:
                    print(f'{row[fieldnames[1]]} {row[fieldnames[2]]} {row[fieldnames[3]]} окончил школу')
                else: 
                    writer.writerow({fieldnames[0]: row[fieldnames[0]], fieldnames[1]: row[fieldnames[1]], 
                        fieldnames[2]: row[fieldnames[2]], fieldnames[3]: row[fieldnames[3]], 
                        fieldnames[4]: f'{stroka}', fieldnames[5]: row[fieldnames[5]], 
                        fieldnames[6]: row[fieldnames[6]], fieldnames[7]: row[fieldnames[7]], 
                        fieldnames[8]: row[fieldnames[8]]})
    print('')

fieldnames = ['ID', 'Фамилия', 'Имя', 'Отчество', 'Класс', 'Литера', 'Дата_рождения', 'Номер_телефона', 'Пометка_перевода']
file_csv = 'class2.csv'

read_base_and_write_csv_file(file_csv, fieldnames)