
with open("game.txt",encoding="utf8") as file:
    file = file.readlines()
    GameName2=[]
    characters2=[]

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

    name=input()
    games=[]
    while name!="game":
        if name not in characters2:
            print("Этого персонажа не существует")
            name = input()
        for i in range(len(characters2)):
            if characters2[i]==name:
                games.append(GameName2[i])
        games = sorted(games)
        games.append("")

        print(f"Персонаж {name} встречается в играх:")
        count=0

        for i in range(len(games)-1):
            if count<5:
                if games[i]!=games[i+1]:
                    print(games[i])
                    count += 1

        if len(games)>5:
            print("и др.")

        games.clear()
        name=input()