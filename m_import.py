import csv


def read_base_and_write_csv_file(file_csv_new, file_csv, fieldnames): # Импортирование нового справочника(csv файл) в основной справочник
    last_id = read_last_id(file_csv)
    print('')
    with open(file_csv_new, encoding='utf8', newline='') as csvfile_in:
        reader = csv.DictReader(csvfile_in)
        with open(file_csv, 'a', encoding='utf8', newline='') as csvfile_out:
            writer = csv.DictWriter(csvfile_out, fieldnames=fieldnames)
            for row in reader:
                writer.writerow({fieldnames[0]: last_id, fieldnames[1]: row[fieldnames[1]], 
                    fieldnames[2]: row[fieldnames[2]], fieldnames[3]: row[fieldnames[3]], 
                    fieldnames[4]: row[fieldnames[4]], fieldnames[5]: row[fieldnames[5]], 
                    fieldnames[6]: row[fieldnames[6]], fieldnames[7]: row[fieldnames[7]], 
                    fieldnames[8]: row[fieldnames[8]]})
                last_id = last_id + 1
    print('')

def new_contact_keyboard_input(file_csv, fieldnames):
    print('')
    print('Введите данные ученика')
    new_contact = []
    for i in range(1, len(fieldnames)):
        new_contact.append(str(input(f'{fieldnames[i]} : ')))
    if new_contact == '':
        new_contact.append('NONE')
    add_new_contact_in_base_shcoolchildren(new_contact, file_csv, fieldnames)
    print('')

def add_new_contact_in_base_shcoolchildren(new_contact, file_csv, fieldnames):
    new_contact.insert(0, read_last_id(file_csv))
    with open(file_csv, 'a', encoding='utf8', newline='') as csvfile_out:
            writer = csv.DictWriter(csvfile_out, fieldnames=fieldnames, restval=None)
            writer.writerow({fieldnames[0]: new_contact[0], fieldnames[1]: new_contact[1], fieldnames[2]: new_contact[2], fieldnames[3]: new_contact[3], 
                fieldnames[4]: new_contact[4], fieldnames[5]: new_contact[5], fieldnames[6]: new_contact[6], fieldnames[7]: new_contact[7], 
                fieldnames[8]: new_contact[8]})

def import_base_shcoolchildren_txt_file(file_csv, fieldnames, file_txt): 
    with open(file_txt, 'r', encoding='utf8') as file:
        new_contact = []
        print('')
        lines = file.readlines()
        for line in lines:
            if line.strip() == '':
                continue
            else:
                new_contact = line.split()
            if len(new_contact) == 8:
                add_new_contact_in_base_shcoolchildren(new_contact, file_csv, fieldnames)
                print(new_contact)
                new_contact = []
            else:
                print(new_contact)
                new_contact = []
                print('Не соответствует формату базы')
        print('')

def read_last_id(file_csv): 
    with open(file_csv, encoding='utf8', newline='') as csvfile:
        last_line = csvfile.readlines()[-1]
        last_line = last_line.strip().split(',')
        last_id = last_line[0]
        if last_id.isdigit() == False:
            last_id = 0
        else:
            last_id = int(last_id)
        return last_id + 1
    
# def new_class(): 
#     with open('class.csv', 'w', encoding='utf8', newline='') as csvfile:
#         fieldnames = ['ID', 'Фамилия', 'Имя', 'Отчество', 'Класс', 'Литера', 'Дата_рождения', 'Номер_телефона', 'Пометка']
#         writer = csv.DictWriter(csvfile, fieldnames=fieldnames, restval=None)

#         writer.writeheader()
#         writer.writerow({'ID': '1', 'Фамилия': 'Озерова', 
#             'Имя': 'Аделина', 'Отчество': 'Артемовна', 'Класс': '5', 'Литера': 'А', 'Дата_рождения': '10.10.2010', 
#             'Номер_телефона': '89123456789', 'Пометка': 'NONE'})