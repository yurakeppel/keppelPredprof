# Открываем файл
with open("game.txt",encoding="utf8") as file:
    file = file.readlines()

    # Создаем отдельные списки для столбцов
    GameName2=[]
    characters2=[]

    # Разделяем строки на списки
    for i in range(len(file)):
        for j in range(len(file[i])):
            if file[i][j]=="$":
                GameName2.append(file[i][:j])
                file[i]=file[i][j+1:]
                break
    for i in range(len(file)):
        for j in range(len(file[i])):
            if file[i][j]=="$":
                characters2.append(file[i][:j])
                file[i]=file[i][j+1:]
                break

    # Ввод имени персонажа
    name=input()
    games=[] # Создаем пустой список игр

    while name!="game": # Пока не введено "game"
        if name not in characters2: # Проверка на существование персонажа
            print("Этого персонажа не существует")
            name = input()

        # Заполняем список играми, в которых встречается персонаж
        for i in range(len(characters2)):
            if characters2[i]==name:
                games.append(GameName2[i])

        # Сортируем список игр
        games = sorted(games)
        games.append("")

        # Выводим первую строку
        print(f"Персонаж {name} встречается в играх:")
        count=0

        # Выводим игры в которых встречается персонаж
        for i in range(len(games)-1):
            if count<5: # Если выведено меньше 5 игр, то продолжаем
                if games[i]!=games[i+1]: # Не выводим если в списке игра повторяется
                    print(games[i])
                    count += 1

        if len(games)>5: # Если в списке больше 5 игр, выводим строку "и др."
            print("и др.")

        games.clear() # Очищаем список
        name=input()