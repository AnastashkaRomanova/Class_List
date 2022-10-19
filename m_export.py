import csv


def export_class_in_txt_file(file_csv, output_txt, klass, litera): # Экспорт одного класса в txt файл
    with open(output_txt, 'w', encoding='utf8') as txtfile:
        with open(file_csv, encoding='utf8', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            titles = reader.fieldnames
            count = 0
            for row in reader:
                if row['Класс'] == klass and row['Литера'] == litera:                 
                    for i in range(len(titles)):
                        txtfile.write(f'{titles[i]} : {row[titles[i]]} \n')
                    txtfile.write('\n')
                    count += 1
            print('')
            print('Найдено совпадений: ', count)
            print('')

def export_in_txt_file(file_csv, output_txt): # Экспорт всего списка в txt файл
    with open(output_txt, 'w', encoding='utf8') as txtfile:
        with open(file_csv, encoding='utf8', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            titles = reader.fieldnames
            for row in reader:
                for i in range(len(titles)):
                    txtfile.write(f'{titles[i]} : {row[titles[i]]} \n')
                txtfile.write('\n')