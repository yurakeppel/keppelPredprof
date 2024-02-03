
with open("game.txt",encoding="utf8") as file:
    file = file.readlines()
    GameNames=[]

    for i in range(len(file)):
        for j in range(len(file[i])):
            if file[i][j]=="$":
                GameNames.append(file[i][:j])
                file[i]=file[i][j+1:]
                break

    GameNames=sorted(GameNames)
    count=1

    for i in range(len(GameNames)-1):
        if GameNames[i]==GameNames[i+1]:
            count+=1
        else:
            print(f"{GameNames[i]} - количество багов: {count}")
            count=1
