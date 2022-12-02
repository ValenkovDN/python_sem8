import view
import export
import imp_data

def button_click():
    temp = view.start()
    while temp != 'q':
        if temp == '1':
            export.exp_data()
        elif temp == '2':
            search = input('Для поиска по id введите "1":\n ' 'Для поиска по фамилии введите "2":\n ''Для поиска по имени введите "3":\n ''Для поиска по отделу введите "4":\n ')
            if search == '1': imp_data.find_id(input('Введите "id": '))
            if search == '2': imp_data.find_surname(input('Введите фамилию: '))
            if search == '3': imp_data.find_name(input('Введите имя: '))
            if search == '4': imp_data.find_department(input('Введите отдел: '))
        temp = view.start()