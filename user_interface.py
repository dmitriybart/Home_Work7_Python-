def get_info ():
    inform = []
    phone_number = ''
    first_name = input('Введите имя: ')
    inform.append(first_name)
    last_name = input('Введите фамилию: ')
    inform.append(last_name)
    valid =False
    while not valid:
            phone_number = input('Введите номер телефона(начиная с 8): ')
            if len(phone_number) != 11:
                print('В номере телефона должно быть 11 цифр.')
            else:
                phone_number = int(phone_number)
                valid = True
    inform.append(phone_number)
    description = input('Введите описание: ')
    inform.append(description)
    return inform