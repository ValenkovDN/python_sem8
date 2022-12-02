import os
import csv
def exp_data():
    if not os.path.exists('company.csv'):
        with open("company.csv", mode="w", encoding='utf-8') as com:
            heading = csv.writer(com, delimiter=';')
            heading.writerow(['id', 'Фамилия', 'Имя', 'Отчество','Телефон', 'Отдел'])
    exit = ''
    while exit != 'q':
        users_data = [
            [input('id: '), input('Фамилия: '), input('Имя: '), input('Отчество: '), input('Телефон: '), input('Отдел: ')]
        ]
        with open("company.csv", mode="a", encoding='utf-8') as com:
            heading = csv.writer(com, delimiter=';')
            heading.writerows(
                users_data
            )
        exit = input('Для завершения работы нажмите "q"\n Для продолжения работы  нажмите "Enter"\n')
