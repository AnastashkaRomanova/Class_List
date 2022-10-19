import csv
import m_import

def search_id(id, file_csv, fieldnames): # Экспорт одного класса в txt файл
    with open(file_csv, encoding='utf8', newline='') as csvfile:
        print('')
        reader = csv.DictReader(csvfile)
        count = 0
        for row in reader:
            if row['ID'] == id:
                print('')
                for i in range(len(fieldnames)):
                    print(f'{fieldnames[i]} : {row[fieldnames[i]]}')
                print('')
                m_import.new_contact_keyboard_input(file_csv, fieldnames)
                print(f'Старый ID[{id}] был удален')
                count += 1
        if count == 0:
            print(f'ID[{id}] - не найден')
        print('')
