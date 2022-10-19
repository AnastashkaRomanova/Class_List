def contact_finder(file_csv, fieldnames):
    seeker = str(input('Введи текст для поиска > '))
    print('')
    seeker = seeker.lower().split()
    with open(file_csv, 'r', encoding='utf8') as file:
        lines = file.readlines()
        count = 0
        for line in lines:
            if line.strip() == '':
                continue
            else:
                seeker_line = line.strip()
                seeker_line_for_search = seeker_line.split(',', 1)[1].lstrip()
                for i in range(0, len(seeker)):
                    if seeker_line_for_search.lower().find(seeker[i]) != -1:
                        if seeker[i] == seeker[-1]:
                            seeker_line = line.strip().split(',')
                            contact_output(seeker_line, fieldnames)
                            count += 1
                            print('')
                        else:
                            continue                            
        print('Найдено совпадений: ', count)
        print('')
    

def contact_output(seeker_line, fieldnames):
    for i in range(len(fieldnames)):
        print(f'{fieldnames[i]} : {seeker_line[i]}')