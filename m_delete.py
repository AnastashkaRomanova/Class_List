import csv

def search_id(id, file_csv):
    with open(file_csv, encoding='utf8', newline='') as csvfile:
        print('')
        reader = csv.DictReader(csvfile)
        count = 0
        for row in reader:
            if row['ID'] == id:                 
                delete_string(id, file_csv)
                print(f'Ученик с ID[{id}] удален')
                count += 1
        if count == 0:
            print(f'ID[{id}] - не найден')
        print('')

def delete_string(id, file_csv):
    file = open(file_csv, 'r', encoding='utf8')
    list_strings = file.readlines()
    file2 = open(file_csv, 'w', encoding='utf8')
            
    array = [line.split(',') for line in list_strings]
    [file2.write((','.join(i))) for i in array if not(i.__contains__(id))]

    file.close 
    file2.close
