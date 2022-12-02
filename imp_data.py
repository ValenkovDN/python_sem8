import os
import csv
import view

def find_id(id):
    if os.path.exists('company.csv'):
        with open("company.csv", mode="r", encoding='utf-8') as com:
            reader = csv.reader(com)
            list = []
            for row in reader:
                if len(row) != 0:
                    list.append(row[0].split(';'))
            count = 0
            for item in list:
                if id == item[0]:
                    view.answer(item)
                    count += 1
            if count == 0:
                view.answer(f'{id} не найден(а)')
    else:
        view.answer('Файл не найден')

def find_surname(surname):
    if os.path.exists('company.csv'):
        with open("company.csv", mode="r", encoding='utf-8') as com:
            reader = csv.reader(com)
            list = []
            for row in reader:
                if len(row) != 0:
                    list.append(row[0].split(';'))
            count = 0
            for item in list:
                if surname == item[1]:
                    view.answer(item)
                    count += 1
            if count == 0:
                view.answer(f'{surname} не найден(а)')
    else:
        view.answer('Файл не найден')

def find_name(name):
    if os.path.exists('company.csv'):
        with open("company.csv", mode="r", encoding='utf-8') as com:
            reader = csv.reader(com)
            list = []
            for row in reader:
                if len(row) != 0:
                    list.append(row[0].split(';'))
            count = 0
            for item in list:
                if name == item[2]:
                    view.answer(item)
                    count += 1
            if count == 0:
                view.answer(f'{name} не найден(а)')
    else:
        view.answer('Файл не найден')

def find_twoname(twoname):
    if os.path.exists('company.csv'):
        with open("company.csv", mode="r", encoding='utf-8') as com:
            reader = csv.reader(com)
            list = []
            for row in reader:
                if len(row) != 0:
                    list.append(row[0].split(';'))
            count = 0
            for item in list:
                if twoname == item[3]:
                    view.answer(item)
                    count += 1
            if count == 0:
                view.answer(f'{twoname} не найден(а)')
    else:
        view.answer('Файл не найден')

def find_phone(phone):
    if os.path.exists('company.csv'):
        with open("company.csv", mode="r", encoding='utf-8') as com:
            reader = csv.reader(com)
            list = []
            for row in reader:
                if len(row) != 0:
                    list.append(row[0].split(';'))
            count = 0
            for item in list:
                if phone == item[4]:
                    view.answer(item)
                    count += 1
            if count == 0:
                view.answer(f'{phone} не найден(а)')
    else:
        view.answer('Файл не найден')

def find_department(department):
    if os.path.exists('company.csv'):
        with open("company.csv", mode="r", encoding='utf-8') as com:
            reader = csv.reader(com)
            list = []
            for row in reader:
                if len(row) != 0:
                    list.append(row[0].split(';'))
            count = 0
            for item in list:
                if department == item[5]:
                    view.answer(item)
                    count += 1
            if count == 0:
                view.answer(f'{department} не найден(а)')
    else:
        view.answer('Файл не найден')