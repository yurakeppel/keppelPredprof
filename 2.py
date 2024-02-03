# Открываем файл
with open("game.txt",encoding="utf8") as file:
    file = file.readlines()

    # Создаем отдельные списки для столбцов
    GameNames=[]

    # Разделяем строки на списки
    for i in range(len(file)):
        for j in range(len(file[i])):
            if file[i][j]=="$":
                GameNames.append(file[i][:j])
                file[i]=file[i][j+1:]
                break

    # Сортировка списка игр по алфавиту
    GameNames=sorted(GameNames)
    count=1
    # Вывод количества ошибок в играх
    for i in range(len(GameNames)-1):
        # Убираем повторы игр
        if GameNames[i]==GameNames[i+1]:
            count+=1
        else:
            print(f"{GameNames[i]} - количество багов: {count}")
            count=1
