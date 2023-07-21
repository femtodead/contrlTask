# Реализовать консольное приложение заметки,с сохранением,чтением, добавлением,редактированием и удалением заметок.
# Заметка должна содержать идентификатор,заголовок,телозаметки и дату/время создания или последнего изменения заметки.
# Сохранение заметок необходимо сделать в формате json или csv формат(разделение полей рекомендуется делать через точку с запятой).
# Реализацию пользовательского интерфейса студент может делать как ему удобнее,можно делать как параметры запуска программы (команда,данные),можно делать 
# как запрос команды с консолии последующим вводом данных,как-то ещё,наусмотрение студента.
import os
from datetime import datetime

def menu (): # меню
    choseUser = input("\nДобавить заметку - 1 \nПоказакать все записи  - 2 \nИзменение заметки - 3 \nУдаление заметки - 4 \nВыход - 5  \nВыберете номер функции: ")
    if choseUser == '1':
        return Create()
    elif choseUser == '2':
        return show()
    elif choseUser == '3':
        return Change()
    elif choseUser == '4':
        return Del()
    elif choseUser == '5':
        print("Пока")
    else:
        print("Номер функции введен не правильно")


def export_note(): # вытаскиавет из файла информацию преобразует его в список по разделителю | возвращает список
    noteList = []
    datapath = os.path.join('.')
    file = open(os.path.join(datapath,"bd.csv"), mode = "r", encoding="utf-8")
    noteList = [el.strip().split("|") for el in file]
    file.close()
    return noteList

def import_note(noteList): # засовыывет в файла информацию из списка добавляя разделитель | 
    datapath = os.path.join('.')
    file = open(os.path.join(datapath,"bd.csv"), mode = "w", encoding="utf-8")
    for el in noteList:
        file.write(f"{el[0]}|{el[1]}|{el[2]}|{el[3]}|{el[4]}\n")
    file.close()

def Create(): # Create: Создание новой записи в записной книге: ввод всех полей новой записи, занесение ее в справочник.
    id = addId(export_note()) 
    time = str(datetime.now()) 
    header = input("Введите заголовок заметки: ") 
    body = input("Введите тело заметки: ") 
    time_last_change = time 
    noteList = export_note()
    noteList.append([id,time,header,body,time_last_change])
    import_note(noteList)
    print("\nЗапись была успешно добавлена\n")
    
    menu()
 
    


def addId(noteList): # это можно заменить на str(len(noteList)-1) но пусть будет
    id = 0
    for el in noteList:
        id +=1
    return str(id)

def show(): # показывает список в определенном формате
    noteList = export_note()
    if  len(noteList) == 0:
        print("\nНет записей\n")
    else:
        for el in noteList:
            print(f"\nid записи {el[0]} создана:{el[1]} \nЗаголовок:{el[2]}\nСодержание:\n {el[3]} \nПоследние изменения: {el[4]}\n")
    menu()

def Del(): # удаление записи по ид
    idnumber = input("Введите id удаляемой записи: ")
    flag = idnumber.isdigit()
    while True:
        if flag == False:
            print("\n Число не дожно содержать знаков (- . + , / и т.д)\n")
            idnumber = input("Введите повторно id удаляемой записи: ")
            if idnumber.isdigit():
                flag = True
        else:
            break
    noteList = export_note()
    elList = []
    sizeIn = len(noteList)
    for el in noteList:
        if el[0] == str(idnumber):
            elList = el
    if len(elList) != 0:
        noteList.remove(elList)
        list_id_change(idnumber,noteList)
        import_note(noteList)
    else:
        print(f"\nЗаметки с id {idnumber} не было найдено")
    menu()

def list_id_change(idnumber,noteList):
    print(idnumber)
    print(len(noteList)-1)
    if int(idnumber) == len(noteList)-1:
        noteList[int(idnumber)][0] = str(idnumber)
    else:
        for i in range(int(idnumber), len(noteList)):
            noteList[i][0] = str(i)

def Change(): # изменение записи по ид
    idnumber = input("Введите id изменяемой записи: ")
    flag = idnumber.isdigit()
    while True:
        if flag == False:
            print("\n Число не дожно содержать знаков (- . + , / и т.д)\n")
            idnumber = input("Введите повторно id изменяемой записи: ")
            if idnumber.isdigit():
                flag = True
        else:
            break
    noteList = export_note()
    choseUser = input("\nИзменить заголовок - 1 \nИзменить тело записи  - 2 \nИзменение заголовок и  тело записи - 3 \nВозврат в меню - 4 \nВыберете номер функции: ")
    if choseUser == '1':
        header = input("Введите новый заголовок заметки: ")
        time_last_change = str(datetime.now())
        noteList[int(idnumber)][2] = header
        noteList[int(idnumber)][4] = time_last_change
        import_note(noteList)
        print("\nЗапись была успешно изменена\n")
    elif choseUser == '2':
        body = input("Введите новое тело заметки: ")
        time_last_change = str(datetime.now())
        noteList[int(idnumber)][3] = body
        noteList[int(idnumber)][4] = time_last_change
        import_note(noteList)
        print("\nЗапись была успешно изменена\n")
    elif choseUser == '3':
        header = input("Введите новый заголовок заметки: ")
        body = input("Введите новое тело заметки: ")
        time_last_change = str(datetime.now())
        noteList[int(idnumber)][2] = header
        noteList[int(idnumber)][3] = body
        noteList[int(idnumber)][4] = time_last_change
        import_note(noteList)
        print("\nЗапись была успешно изменена\n")
    elif choseUser == '4':
        return menu()
    else:
        print("Номер функции введен не правильно")
    menu()

menu()