import csv

# Открываем файл
with open("game.txt",encoding="utf8") as file:
    file = file.readlines()

    # Создаем отдельные списки для столбцов
    GameName=[]
    characters=[]
    nameError=[]
    date=[]

    # Разделяем строки на списки
    for i in range(len(file)):
        for j in range(len(file[i])):
            if file[i][j]=="$":
                GameName.append(file[i][:j])
                file[i]=file[i][j+1:]
                break
    for i in range(len(file)):
        for j in range(len(file[i])):
            if file[i][j]=="$":
                characters.append(file[i][:j])
                file[i]=file[i][j+1:]
                break
    for i in range(len(file)):
        for j in range(len(file[i])):
            if file[i][j]=="$":
                nameError.append(file[i][:j])
                file[i]=file[i][j+1:]
                break
    for i in range(len(file)):
        date.append(file[i][:-1])

    # Ищем ошибки с номером 55, после чего заеняем номер ошибки на "Done", а дату на "0000-00-00"
    for i in range(len(nameError)):
        if "55" in nameError[i]:
            print(f"У персонажа {characters[i]} в игре {GameName[i]} нашлась ошибка с кодом: {nameError[i]} Дата фиксации: {date[i]}")
            nameError[i]="Done"
            date[i]="0000-00-00"

# Записываем данные в новый файл "game_new.csv"
with open("game_new.csv","w",encoding="utf8") as f:
    f = csv.writer(f,lineterminator="\n")
    for i in range(len(file)):
        f.writerow([GameName[i]+"$"+characters[i]+"$"+nameError[i]+"$"+date[i]])

