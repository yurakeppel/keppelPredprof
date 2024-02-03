import csv

with open("game.txt",encoding="utf8") as file:
    file = file.readlines()
    GameName=[]
    characters=[]
    nameError=[]
    date=[]
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

    for i in range(len(nameError)):
        if "55" in nameError[i]:
            print(f"У персонажа {characters[i]} в игре {GameName[i]} нашлась ошибка с кодом: {nameError[i]} Дата фиксации: {date[i]}")
            nameError[i]="Done"

with open("game_new.csv","w",encoding="utf8") as f:
    f = csv.writer(f,lineterminator="\n")
    for i in range(len(file)):
        f.writerow([GameName[i]+"$"+characters[i]+"$"+nameError[i]+"$"+date[i]])

